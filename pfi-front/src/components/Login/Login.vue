<template>
  <div class="login">
      <div class="imageCover">
        <div class="degradado">
        <div class="container-fluid container-login">
         
            <div class="row d-flex justify-content-center align-items-center">
              <h1 class="title">Bienvenido a Formación Integral</h1>
              <img
                src="../../assets/logo-ujed.png"
                alt="img-ujed"
                style="max-width: 230px; min-width: 230px; padding: 20px;"
              />
              <p class="text-google">Ingresa con tu correo electronico y contraseña</p>
              
              <form class="form-signin" @submit.prevent="handleSubmit">
                <v-text-field
                label="Correo Electronico"
                variant="regular"
                placeholder="Placeholder"
                v-model="email"
                background-color="white"
              ></v-text-field>

                <v-text-field
                label="Contraseña"
                variant="regular"
                placeholder="Placeholder"
                v-model="password"
                background-color="white"
                type="password"
                ></v-text-field>
                <v-btn
                  block
                  class="text-none"
                  color="#FFFFFF"
                  size="x-large"
                  variant="flat"
                  type = "submit"
                  
                >
                  Iniciar sesión
                </v-btn>
              
                
              </form>
            </div>
          
        </div>
        </div>
        <!--Alerta para los correos electronicos-->
        <div v-if="showEmailAlert" class="alert alert-danger Alert-center-text" role="alert">
               <p> La dirección de correo electrónico debe terminar con @ujed.mx</p>
        </div>

        <!--Alerta para las contraseñas-->
        <div v-if="errorPassword" class="alert alert-danger Alert-center-text" role="alert">
            <p>Error credenciales incorrectas</p>
        </div>
      </div>
    
  </div>
</template>

<script>
import axios from 'axios'; 

export default {
  name: "login",
  props: {
    msg: String,
  },
  data(){
    return{
      email:'', 
      password:'', 
      showEmailAlert: false,
      errorPassword: false,
      user: null,
    }; 
  }, 
  methods: {
    async handleSubmit(){
      if(!this.email.endsWith('@ujed.mx')){
        this.showEmailAlert = true; 
        this.errorPassword = false;
        console.log("Alerta");
      }else{
        try{
        const response = await axios.post("http://127.0.0.1:8001/alumnos/login/", {
          email: this.email, 
          password: this.password, 
        });

        sessionStorage.setItem('jwtToken', response.data.token); 

        console.log(response.data); 
        window.location.href = "/inicio"
        }catch(error){
          console.error("error al enviar la solicutd ", error)
          this.errorPassword = true; 
          this.showEmailAlert = false; 
          console.log("Contraseña incorrecta")
        }
      }

     
    }, 
   

  },

};
</script>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>


.Alert-center-text{
  text-align: center;

}

.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}.form-signin {
  width: 100%;
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .checkbox {
  font-weight: 400;
}
.form-signin .form-control {
  position: relative;
  box-sizing: border-box;
  height: auto;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
.login {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow-x: hidden;
}

.title{
  font-size: 15px;
  font-weight: 600;
  margin-top: 10px;
  margin-bottom: 10px;
  text-align: center;
  padding: 10px;
  color: black;
  text-transform: uppercase;
}

.imageCover{
 position: relative;
 width: 100vw;
 height: 100vh;
 overflow-x: hidden;
}

.imageCover::before{
  content:""; 
  background-image: url("../../assets/cover-lg.jpg");
  background-size: cover;
  background-position: center;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  
}

.degradado{
  background: linear-gradient(to top, rgba(15, 46, 61, 0.5), rgba(15, 46, 61, 0) 100%);
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  
} 

.text-google {
  font-size: 15px;
  font-weight: 600;
  margin-top: 10px;
  margin-bottom: 10px;
  text-align: center;
  padding: 10px;
  color: black;
} 

.container-login {
  display: flex;
  justify-content: center;
  align-self: center;
  border: 2px solid #1111;
  background-color: #EEEEEE;
  min-width: 30%;
  max-width: 30%;
  margin-top: 10%; 
}


</style>
