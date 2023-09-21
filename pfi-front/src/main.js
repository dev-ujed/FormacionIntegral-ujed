import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './router'
// //@eslint-disable-next-line
// //@ts-ignore
// import gAuth from 'vue3-google-auth'

// const GAuth = gAuth.createGAuth({
//   client_id:'341888786205-bhre3nmhcsvp3hrilkmalmp4lt6f39ed.apps.googleusercontent.com'
// })

// console.log(GAuth)
// const CLIENTID = "910843871488-9ssv3lop0mfpo3ml14sr6in3qft6d5ja.apps.googleusercontent.com"


// import GAuth from 'vue-google-oauth2'
// const gauthOption = {
//   clientId: '341888786205-bhre3nmhcsvp3hrilkmalmp4lt6f39ed.apps.googleusercontent.com',
//   prompt: 'select_account'
// }
// Vue.use(GAuth, gauthOption)

Vue.config.productionTip = false;

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
