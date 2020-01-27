<template>
  <div>
    <div class="box" v-for="item in products" :key="item.id">
      <p>{{ item.title }}</p>
    </div>
    <br />
  </div>
</template>


<script>
import axios from 'axios'

export default {
  data(){
    return {
      products : null
    }
  },
  mounted(){
    let self = this 
    axios.get( 'http://localhost:5000/get/products')
    .then(function(response){
      self.products = response.data.products

    })
    
  }
  
}
</script>