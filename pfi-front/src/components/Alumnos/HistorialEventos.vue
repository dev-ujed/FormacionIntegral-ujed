<template>
    <div>
        <drawer/>
        <v-container id="createFile">
      <v-row id="datosAlumno">
        <v-card class="elevation-8">
            <v-card-title>Datos del Alumno</v-card-title>
            <v-row>
                <v-col
                align-self: center
                xs="12"
                sm="12"
                md="4">
                    <v-img
                    :lazy-src="dataAlumno.img"
                    max-height="150px"
                    max-width="250px"
                    :src="dataAlumno.img"
                    object-fit="cover"
                    ></v-img>
                </v-col>
                <v-col 
                align-self: center
                xs="6"
                sm="6"
                md="4">
                    <v-card-text>
                        <label><strong>Alumno: </strong></label>
                        <v-spacer></v-spacer>
                        <label>{{ dataAlumno.nombre }}  {{dataAlumno.paterno}} {{dataAlumno.materno}}</label>
                        <v-spacer></v-spacer>
                        <label><strong>Matricula: </strong></label>
                        <v-spacer></v-spacer>
                        <label>{{ dataAlumno.cve_alumno }} </label>
                    </v-card-text>
                </v-col>
                <v-col 
                align-self: center
                xs="6"
                sm="6"
                md="4"
                >
                    <v-card-text>
                        <label><strong>Carrera: </strong></label>
                        <v-spacer></v-spacer>
                        <label></label>
                        <v-spacer></v-spacer>
                        <label><strong>Semestre: </strong></label>
                        <v-spacer></v-spacer>
                        <label></label>
                        <v-spacer></v-spacer>
                        <label><strong>Correo electronico: </strong></label>
                        <v-spacer></v-spacer>
                        <label>{{ dataAlumno.cve_alumno }}@alumnos.ujed.mx</label>
                    </v-card-text>
                </v-col>
            </v-row>
        </v-card>
      </v-row>
      <v-row style="margin-top: 20px">
        <v-col>
            <v-card-title>Historial de eventos</v-card-title>
        </v-col>
        <v-col>
            <v-card-title>Total de creditos: {{totalCreditos}}</v-card-title>
        </v-col>
      </v-row>
        
      <v-row id="historialEventos" style="margin-top: 30px"
        v-for="(item, index) in eventsAlumno" :key="index">
          <v-card class="elevation-8">
            <v-row>
                <v-col>
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-title>{{item.tituloEvento}}</v-list-item-title>
                            <v-list-item-subtitle>
                            {{item.descripcionEvento}}
                            </v-list-item-subtitle>
                            <v-list-item-subtitle>
                            Fecha: {{item.fechaEvento}}
                            </v-list-item-subtitle>
                        </v-list-item-content>
                    </v-list-item>
                </v-col>
                <v-col>
                    <v-list-item three-line>
                        <v-list-item-content>
                            <v-list-item-subtitle>Responsable: {{item.unidadResponsable}}</v-list-item-subtitle>
                            <v-list-item-subtitle>
                            Sede: {{item.sede}}
                            </v-list-item-subtitle>
                            <v-list-item-subtitle>
                            Creditos: {{item.creditos}}
                            </v-list-item-subtitle>
                        </v-list-item-content>
                        <v-list-item-action>
                            <v-list-item-action-text></v-list-item-action-text>

                            <v-icon
                                v-if="item.asistencia == 0"
                                color="red"
                                aria-label="No asistio"
                            >
                                mdi-close-circle
                            </v-icon>

                            <v-icon
                                v-else-if="item.asistencia == 1"
                                color="teal"
                                aria-label="asistio"
                            >
                                mdi-check-decagram
                            </v-icon>

                            <v-icon
                                v-else
                                color="gray"
                                aria-label="Sin asitencia"
                            >
                                mdi-alert-decagram
                            </v-icon>
                            
                        </v-list-item-action>
                    </v-list-item>
                </v-col>
            </v-row>
        </v-card>
      </v-row>
      <v-speed-dial
        v-model="fab"
        top
        right
        :direction="direction"
        :open-on-hover="hover"
        :transition="transition"
      >
        <template v-slot:activator>
            <v-btn
                v-model="fab"
                color="#a4010b"
                dark
                fab >
                <v-icon v-if="fab">
                    mdi-close
                </v-icon>
                <v-icon v-else>
                    mdi-file-export
                </v-icon>
            </v-btn>
        </template>
        <v-btn
            fab
            dark
            color="green"
        >
            <download-excel
                class=""
                :data="eventsDataFiles"
                :fields="json_fields"
                type = "xls"
                :name="`${this.fileName}_${this.heading}.xls`"
                :header="alumnoExcel"
                :footer ="`Creditos validados: ${this.totalCreditos}`"
            >
                <v-icon>mdi-file-excel</v-icon>
            </download-excel>
        </v-btn>
        <v-btn
            fab
            dark
            color="red"
            @click="createPDF()"
        >
            <v-icon>mdi-file-pdf-box</v-icon>
        </v-btn>
    </v-speed-dial>
        </v-container>

    </div>
  
</template>

<script>
import AlumnosDataService from "../../services/AlumnosDataService";
import FormacionInDataService from "../../services/FormacionInDataService";
import drawer from "../Drawer/Drawer.vue"; 

/* import html2canvas from "html2canvas";*/
import jsPDF from "jspdf"; 
import 'jspdf-autotable';
import downloadExcel from "vue-json-excel";

export default {
  name: "HistorialEventos",
  data() {
    return {
      dataAlumno: [],
      eventsAlumno: [],
      totalCreditos: 0,
      alumnoDataFiles: [],
      eventsDataFiles: [],
      fileName: '',
      alumnoExcel: '',
      heading: "Eventos",
      direction: 'bottom',
      fab: false,
      fling: false,
      hover: true,
      top: true,
      right: true,
      transition: 'slide-y-reverse-transition',
      json_fields: {
        "Evento": "tituloEvento",
        "Unidad Responsable": "unidadResponsable",
        "Despcripción": "descripcionEvento",
        "Fecha del evento": "fechaEvento",
        "Sede": "sede",
        "Creditos de evento": "creditos",
        "Asistencia" :"asistencia"
      },
    };
  },
  created() {
      this.getAlumno();
      this.getEventsAlumno(); 
  },
  mounted() {
      
  },
  components: {
      downloadExcel, 
      drawer
  },
  methods: {
    getAlumno() {
        AlumnosDataService.getOaloumno(this.$route.params.id)
            .then(response => {
                console.log(response.data)
                this.dataAlumno = response.data;
                this.alumnoDataFiles.push(response.data);
                this.fileName = response.data.cve_alumno  ;
                this.alumnoExcel = "Alumno: "+ response.data.nombre + "  " + response.data.paterno + " " + response.data.materno + "  " + "Matricula: " + response.data.cve_alumno + "  "  + "Carrera: " + response.data.cve_escuela + "  " + "Semestre: " + "1";
            })
            .catch(e =>{
                console.log(e);
            })
    },

    getEventsAlumno(){
        FormacionInDataService.getEventsAlumno(this.$route.params.id)
        .then(response => {
            this.eventsAlumno = response.data;
            console.log(this.eventsAlumno);
            this.validarCreditos(response.data);
        })
        .catch(e => {
            console.log(e);
        })
    },

    validarCreditos(response){
        this.eventsDataFiles = [];
        for (let evento of response) {
            var creditos = parseFloat(this.totalCreditos);
            var creditos2 = parseFloat(evento.creditos);
            if(evento.asistencia == 1){
                var res = creditos + creditos2;
                this.totalCreditos =  res;
            }
            this.createData(evento);
        }
    },
    
    createData(response){
        var status;
        if( response.asistencia == 1){
            status = "Asistió";
        } else if(response.asistencia == 0) {
            status = "No asistió";
        } else {
            status = "Aún no se aplicó asistencia"
        }
        var data = {
            tituloEvento: response.tituloEvento,
            unidadResponsable: response.unidadResponsable,
            descripcionEvento: response.descripcionEvento,
            eventoDedicadoA: response.eventoDedicadoA,
            fechaEvento: response.fechaEvento,
            inicioEvento: response.inicioEvento,
            finEvento: response.finEvento,
            sede: response.sede,
            cupo: response.cupo,
            descripcion: response.descripcion,
            creditos: response.creditos,
            categorias: response.categorias,
            asistencia: status
        };
        this.eventsDataFiles.push(data);
    },
    createPDF(){
        const doc = new jsPDF({
            orientation: "portrait",
            unit: "in",
            format: "letter"
        });

        const image = new Image(); 
        image.src = "data:image/png;base64,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";

        doc.addImage(image, "PNG", 0.4, 0.4 , 1.0, 0.7);


        // text is placed using x, y coordinates
        doc.setFontSize(16).text("Historial de eventos", 3.2, 0.7);
        doc.setFontSize(16).text("Total de creditos: "+ this.totalCreditos, 6, 0.7);
        // create a line under heading 
        doc.setLineWidth(0.01).line(0.5, 1.1, 8.0, 1.1);
        doc.autoTable({
            headStyles: { fillColor: [199, 0, 57] },
            body: this.alumnoDataFiles,
            columns: [
                { header: 'Nombre', dataKey: 'nombres' },
                { header: 'Apellido', dataKey: 'apellidos' },
                { header: 'Matricula', dataKey: 'matricula' },
                { header: 'Carrera', dataKey: 'carrera' },
                { header: 'Semestre', dataKey: 'semestre' }
            ],
            margin: { left: 0.5, top: 1.3 }
        });

        doc.setLineWidth(0.01).line(0.5, 3.1, 8.0, 3.1);
        doc.autoTable({
            headStyles: { fillColor: [199, 0, 57] },
            body: this.eventsDataFiles,
            columns: [
                { header: 'Eventos', dataKey: 'tituloEvento' },
                { header: 'Creditos', dataKey: 'creditos' },
                { header: 'Asistencia', dataKey: 'asistencia'}
            ],
            margin: { left: 0.5, top: 40.5 }
        });
        const backgroundfooter = [150, 20, 41]; 
        const colorText = [255, 255, 255];
        doc
        .setFillColor(backgroundfooter[0], backgroundfooter[1], backgroundfooter[2])
        .rect(-0.1, doc.internal.pageSize.height - 0.3, 10, 0.5, "F"); 

        doc
        .setFont("times")
        .setFontSize(11)
        .setTextColor(colorText[0], colorText[1], colorText[2])
        .text(
          "Constitución 404 Sur, Zona Centro. C.P. 34000, Durango, Dgo. México. Tel: (618) 827 12 00. ujed@ujed.mx",
          1.0,
          doc.internal.pageSize.height - 0.10
        )
      
            .save(`${this.fileName}_${this.heading}.pdf`);
    },
  }
}
</script>

<style>
    #createFile .v-speed-dial {
        position: absolute;
    }

    #createFile .v-btn--floating {
        position: relative;
    }

   
</style>