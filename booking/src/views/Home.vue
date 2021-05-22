<template>
<div>
  <img src="../assets/forsidebilde.jpeg" class="forside_img" alt="forsidebilde">
  <div class="container">
    <br>
    <div class="row row-cols-2 row-cols-lg-3 g-2 g-lg-3">

      <div class="col" v-for="item in BookingItems" :key="item">
        <div class="p-3 border bg-light element">
         <!--
          {% if {{item.img}} == "../assets/Berghans.jpeg" %}
          <img src="../assets/Berghans.jpeg" alt="">
          {% if {{item.img}} == "../assets/k2ski.jpeg" %}
          <img src="../assets/k2ski.jpeg" alt="">
          {% if {{item.img}} == "../assets/sovepose.jpeg" %}
          <img src="../assets/sovepose.jpeg" alt="">
          {% if {{item.img}} == "../assets/Salomon.jpeg" %}
          <img src="../assets/Salomon.jpeg" alt="">
          {% if {{item.img}} == "../assets/frostsko.png" %}
          <img src="../assets/frostsko.png" alt="">
          {% endif %}
        -->
          <img src="../assets/Berghans.jpeg" alt="berghans">
          <br>
          <h3>{{item.name}} </h3>
          <p> {{item.description}} </p>
          <button type="button" class ="btn btn-primary">
            <router-link v-if="!IsLoggedIn" to= "/login" class="nav-link activate" aria-current="page">Book</router-link>
            <router-link v-if="IsLoggedIn" to= "/profile" class="nav-link activate" aria-current="page">Book</router-link>
          </button>
        </div>
      </div>

    </div>
  </div>

</div>
</template>


<style>
.forside_img{
  width: 100%;
  height: 800px;
}


img{
  width: 300px;
  height: 300px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>



<script>
import { useStore } from "vuex";
import { computed } from '@vue/runtime-core';

export default {
  name: 'Home',
  setup(){
    const store = useStore();
    const BookingItems = store.getters.get_BookingItems;
    const IsLoggedIn = computed(() => store.getters.IsLoggedIn)
    console.log(BookingItems)

    return {
      BookingItems,
      IsLoggedIn,
    }
  }
};
</script>