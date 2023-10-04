<template>
  <div>
    <drawer/>
    <v-container>
      <v-row>
        <v-data-table
          :headers="headers"
          :items="alumnos"
          :search="search"
          item-key="id"
          class="elevation-1"
        >
          <template v-slot:top>
            <v-toolbar-title class="px-3 py-2">Estudiantes</v-toolbar-title>
            <v-toolbar flat>
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Buscar alumnos"
                  single-line
                  hide-details
                ></v-text-field>
            </v-toolbar>
          </template>
          <template v-slot:item.detalles="{ item }">
          <v-btn
              class="ma-2"
              @click="sendStudent(item.cve_alumno)"
            >
              <v-icon>
                mdi-account-details
              </v-icon>
            </v-btn>
          </template>
        </v-data-table>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import AlumnosDataService from "../../services/AlumnosDataService";
import drawer from "../Drawer/Drawer.vue"; 

export default {
    name: "alumnos",
    data() {
      return {
        alumnos: [],
        search: '',
        headers: [
          { text: 'Matricula', align: 'center', sortable: true, value: 'cve_alumno'},
          { text: 'Nombres', value: 'alumno.nombre' },
          { text: 'Apellido paterno', value: 'alumno.paterno' },
          { text: 'Apellido materno', value: 'alumno.materno' },
          { text: 'Carrera', sortable: true, value: 'desc_carrera' },
          { text: 'Semestre', align: 'center', value: 'semestre' },
          { text: 'Ver detalles', align: 'center', value: 'detalles'}
        ],
      };
    },
    components:{
      drawer
    },
    methods: {
      retrieveAlumnos() {
        AlumnosDataService.getoalumnos()
          .then(response => {
            this.alumnos = response.data;
            console.log(this.alumnos);
          })
          .catch(e => { 
            console.log(e);
          });
      },
      
      

      sendStudent(id) {
        console.log(id)
        this.$router.push("/fi-alumnos/"+id); 
      },


      
    },
    async mounted() {
      // this.retrieveAlumnos();


      const token = sessionStorage.getItem("jwtToken"); 

      if(token){
        axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;

        try{
          const response = await axios.request('http://127.0.0.1:8001/alumnos/get_coordinator');
          this.alumnos = response.data; 
          console.log(this.alumnos);
        }catch(error){
          console.error('Error', error);
        }
      }
      else{
        console.error('No token')
      }
    }
}
</script>

<style>

</style>