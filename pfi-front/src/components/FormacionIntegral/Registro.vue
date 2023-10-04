<template>
  <div>
  <drawer/>
  <v-container>
    <v-row>
      <v-col>
        <v-btn
          depressed
          elevation="2"
          block
          color = "#a4010b"
          class="white--text"
        >Registro</v-btn>
      </v-col>
      <v-col>
        <v-btn
          v-if="categoria != 'Externos'"
          depressed
          elevation="2"
          plain
          block
          @click="sendEvent()"
        >Asistencia</v-btn>
        <v-btn
          v-else
          depressed
          elevation="2"
          plain
          block
          @click="sendEvent()"
        >Validación de creditos</v-btn>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <v-data-table
          v-model="selected"
          :headers="headers"
          :items="alumnos"
          :search="search"
          item-key="cve_alumno"
          item-selectable="selectable"
          show-select
          class="elevation-8 overflow-auto"
          height="520px"
        >
        
          <template v-slot:top>
            <v-toolbar flat>
              <v-toolbar-title>Estudiantes</v-toolbar-title>
              <v-spacer></v-spacer>
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Buscar Estudiantes"
                  single-line
                  hide-details
                ></v-text-field>
            </v-toolbar>
          </template>
          <template v-slot:no-data>
            No se encuentran estudiantes registrados actualmente!
          </template>
        </v-data-table>
      </v-col>
      <v-col>
        <v-row>
          <v-col>
            <v-toolbar-title>{{evento.tituloEvento}}</v-toolbar-title>
          </v-col>
          <v-col>
            <v-toolbar-title>Cupo de evento total: {{ evento.cupo }}</v-toolbar-title>
            <v-toolbar-title v-if="evento.cupo - alumnosRegistrados - selected.length > 0">Disponible: {{evento.cupo - alumnosRegistrados - selected.length}}</v-toolbar-title>
            <v-toolbar-title v-else>No hay más lugares disponibles</v-toolbar-title>
          </v-col>
        </v-row>
        <v-row align="center">
          <v-data-table
            dense
            :headers="headersRegistrados"
            :items="selected"
            item-key="name"
            class="elevation-8 overflow-auto"
            max-height="520px"
            v-if="selected.length != 0"
          >
            <template v-slot:top>
              <v-toolbar flat>
                <v-btn
                  block
                  depressed
                  color="#a4010b"
                  class="white--text"
                  @click="validarAlumnos()"
                >Registrar Estudiantes
              </v-btn>
              </v-toolbar>
            </template>
            <template v-slot:item.nombre="{ item }">
                {{ item.alumno.nombre}}  {{item.alumno.paterno}}  {{ item.alumno.materno }}
            </template>
          </v-data-table>
          <v-data-table
            item-key="name"
            class="elevation-8 overflow-auto"
            max-height="480px"
            loading
            loading-text="Seleccionar estudiantes para registrar"
            v-else
          >
            <template v-slot:no-data>
              No se encuentran estudiantes registrados actualmente!
            </template>
          </v-data-table>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
  </div>
</template>

<script>

import FormacionInDataService from "../../services/FormacionInDataService";
import EventosDataService from "../../services/EventosDataService";
import swal from 'sweetalert';
import drawer from  "../Drawer/Drawer.vue"; 
import axios from "axios";

export default {
    name: "registro",
    data() {
      return {
        alumnos: [],
        singleSelect: true,
        selected: [],
        evento: [],
        search: '',
        alumnosRegistrados: 0,
        disponible: 0,
        count: 0,
        categoria: '',
        headers: [
          { text: 'Matricula', align: 'start', sortable: true, value: 'cve_alumno'},
          { text: 'Nombres', value: 'alumno.nombre' },
          { text: 'Paterno', value: 'alumno.paterno' },
          { text: 'Materno', value: 'alumno.materno' },
          { text: 'Carrera', sortable: true, value: 'desc_carrera' },
          { text: 'Semestre', value: 'semestre' }
        ],
        headersRegistrados: [
          { text: 'Nombre', align: 'start', sortable: false, value: ('alumno.nombre')},
          {text: 'Apellido paterno', align:'start', sortable: false, value: ('alumno.paterno')},
          {text: 'Apellido materno', align:'start', sortable: false, value: ('alumno.materno')},
          { text: 'Matricula', align: 'start', sortable: false, value: 'cve_alumno'},
        ],
        registro: {
          id: null,
          nombre: "",
          matricula: "",
          asistencia: null,
          evento: null,
          alumno: null,
        },
      };
    },
    components:{
      drawer
    }, 
    methods: {
      retrieveAlumnos() {
        
      },

      sendEvent() {
        if(this.categoria != 'Externos') {
          this.$router.push("/fi-asistencia/"+this.$route.params.id);
        }
        else {
          this.$router.push("/fi-validacion/"+this.$route.params.id);
        }
        
      },
      validarAlumnos(){
        this.obtenerDisponible();
        if(this.disponible >= 0){
          for (let alumno of this.selected) {
            FormacionInDataService.getUserExist(this.$route.params.id, alumno.matricula)
              .then(response => {
                if(response.data.length == 1){
                  console.log("alumno existente: " + alumno.alumno.nombre + ' ' + alumno.alumno.paterno + ' ' + alumno.alumno.materno);
                } else {
                  console.log("alumno registrado: " + alumno.alumno.nombre + ' ' + alumno.alumno.paterno + ' ' + alumno.alumno.materno);
                  this.registrarAlumnos(alumno);
                }
              })
              .catch(e =>{
                console.log(e)
              });
          }
        }else{
          swal("Excedio el limite de lugares disponibles","","warning")
        }     
        setTimeout(this.sendEvent, 1000);   
      },
      
      registrarAlumnos(alumno){
        var data = {
          nombre: alumno.alumno.nombre + ' ' + alumno.alumno.paterno + ' ' + alumno.alumno.materno,
          matricula: alumno.cve_alumno,
          asistencia: null,
          evento: this.$route.params.id,
          
        }
        FormacionInDataService.create(data)
          .then(response => {
            this.eventos.id = response.data.id;
            console.log(response.data);
          })
          .catch(e => {
            console.log(e);
          });
      },
      
      infoEvento(){
        EventosDataService.getevento(this.$route.params.id)
            .then(response => {
                this.evento = response.data
            })
            .catch(e => {
                console.log(e)
            });
      },
      numAlumnos() {
        FormacionInDataService.getAll(this.$route.params.id)
          .then(response => {
            this.alumnosRegistrados = response.data.length;
          })
          .catch(e => {
            console.log(e);
          });
      },
      obtenerDisponible(){
        this.disponible = this.evento.cupo - this.alumnosRegistrados - this.selected.length;
      },
      
      getEvent(){
        EventosDataService.getevento(this.$route.params.id)
          .then(response => {
            this.categoria = response.data.categorias;
          })
          .catch(e => {
            console.log(e);
          });
      },
    },
    async mounted() {

      const token = sessionStorage.getItem("jwtToken"); 

      if(token){
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
        try{
          const response = await axios.request('http://127.0.0.1:8001/alumnos/get_coordinator'); 
          this.alumnos = response.data; 
        }catch(error){
          console.log('Error', error); 
        }
      }else{
        console.log('No token')
      }
    },
    created() {
      this.retrieveAlumnos();
      this.infoEvento();
      this.numAlumnos();
      this.getEvent();
    }
}
</script>

<style>

</style>