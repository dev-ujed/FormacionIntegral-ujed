<template>
    <div class="login">
      <div class="imageCover">
        <div class="degradado">
          <div class="container-fluid container-login">
            <div class="row d-flex justify-content-center align-items-center">
              <h1 class="title">Bienvenido a Formación Integral</h1>
              <img
                src="../../assets/uje-removebg-preview.png"
                alt="img-ujed"
                style="max-width: 230px; min-width: 230px; padding: 20px;"
              />
              <p class="text-google">Registra en Formación Integral</p>
  
              <form class="form-signin" @submit.prevent="submit">
      
                <v-text-field
                label="Correo Electronico"
                single-line
                variant="solo"
                v-model="formData.email"
                background-color="white"
              ></v-text-field>

              <v-text-field
                label="Contraseña"
                single-line
                variant="outlined"
                v-model="formData.password"
                background-color="white"
                type="password"
                ></v-text-field>
                <v-text-field
                label="Contraseña"
                single-line
                variant="outlined"
                v-model="formData.password_confirm"
                background-color="white"
                type="password"
                ></v-text-field>
  
                <v-btn
                  block
                  class="text-none"
                  color="grey-lighten-3"
                  size="x-large"
                  variant="flat"
                  type = "submit"
                >
                  Registrarte
                </v-btn>
                <router-link to="/">
                  <p class="text-signup">Ya tienes una cuenta, da click aqui</p>
                </router-link>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
import axios from 'axios';


export default {
  data() {
    return {
      formData: {
        email: '',
        password: '',
        passwordConfirm: '',
      },
    };
  },

  methods: {
    submit() {
      

      axios
        .post('http://127.0.0.1:8000/alumnos/register/', this.formData)
        .then(response => {
          console.log(response)
          window.location.href = '/inicio'
        })
        .catch(error => {
          console.log(error);
        });
    },
  },
};
  </script>
  
  <style scoped>

  .text-signup{
    text-align: center;
    color: white;
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
  color: #fff;
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
  background: linear-gradient(to bottom, rgba(65, 84, 93, 0.5), rgb(10, 21, 27));
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
  color: #fff;
} 

.container-login {
  display: flex;
  justify-content: center;
  align-self: center;
  border: 2px solid #1111;
  background-color: #b01b30;
  min-width: 30%;
  max-width: 30%;
  margin-top: 10%; 
}

.google-button {
  box-shadow: 1px 1px 3px #0000001a;
  background-color: #111111;
  display: flex;
  margin: auto;
    margin-top: auto;
    margin-bottom: auto;
  margin-bottom: 20px;
  margin-top: 20px;
  padding: 3px;
  width: 230px;
  height: 48px;
  float: righ
}

.google-button__icon {
  background: #fff;
  border-radius: 3px;
  display: flex;
  height: 40px;
  justify-content: center;
  width: 40px;
}

.google-button__text {
  align-self: center;
  color: #fff;
  text-align: center;
  width: 184px;
}

  </style>
  