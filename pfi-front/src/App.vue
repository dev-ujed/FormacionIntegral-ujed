<template>
  <v-app>
    <!-- Sizes your content based upon application components -->
    <v-main>

      <!-- Provides the application the proper gutter -->
     
        <router-view></router-view>
      
    </v-main>

 
  </v-app>
</template>
<script src="https://accounts.google.com/gsi/client" async defer></script>


<script>


export default {
  name: 'app',

};



</script>

<style>
  
  .formacion_text{
    color:white; 
  }
</style>