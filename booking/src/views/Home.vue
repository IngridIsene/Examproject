<template>
<div>
  <div class="parallax"></div>
  <!-- <img src="../assets/forsidebilde.jpeg" class="forside_img" alt="forsidebilde"> -->
  <div class="container">
    <br>
    <form class="d-flex">
      <input class="form-control me-2" type="text" v-model="searchQuery" placeholder="Search for products by name" aria-label="Search" id="homesearch">
      <div class="dropdown">
        <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenu2" data-bs-toggle="dropdown" aria-expanded="false">
          Sort By
        </button>
        <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
          <li><button @click="sortLowHigh" class="dropdown-item" type="button">Price (Low - High) </button></li>
          <li><button @click="sortHighLow" class="dropdown-item" type="button">Price (High - Low)</button></li>
          <li><button @click="sortOldNew" class="dropdown-item" type="button">Oldest to Newest Ads</button></li>
          <li><button @click="sortNewOld" class="dropdown-item" type="button">Newest to Oldest Ads</button></li> 
        </ul>
      </div>
    </form>
    
    <div class="bookings row row-cols-2 row-cols-lg-3 g-2 g-lg-3">

      <div class="col" v-for="item in resultQuery" :key="item">
        <div class="p-3 border bg-light element">
          <img v-bind:src="require(`../assets/${item.img}`)" alt="">
          <br>
          <h3>{{item.name}} </h3>
          <p> {{item.description}} </p>
          <p> {{item.price}} kr,- </p>
          <button v-if="!IsLoggedIn" type="button" class ="btn btn-primary">
            <router-link to= "/login" class="nav-link activate" aria-current="page">Book</router-link>
          </button>
          <button v-if="IsLoggedIn" @click="toBooking(item)" type="button" class ="btn btn-primary">Book</button>
        </div>
      </div>

    </div>
  </div>

  <footer>
    <div class="main_footer">
      <div class="contact_information">
        <p>Customer service | customer_service@booking.com | Telephone: 9892759201</p>
      </div>
    </div>
  </footer>

</div>
</template>


<style>

.parallax {
  background-image:url("../assets/forsidebilde.jpeg");
  min-height: 550px;
  width: 100%;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat; 
  background-size: cover;
}

.bookings {
  min-height: 20vh;
  padding-top: 20px;
  padding-bottom: 20px;
}

img{
  width: 300px;
  height: 300px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.p-3 img:hover {
color:#d8ac9c;
background-color: #EFD9D1;
text-decoration: none;
border: 5px solid #999b84;
}
 
.btn {
background-color: #e4d3cf;
border-color: #5b6d5b;
color: black;
}

#homesearch{
  width:50%;
}

.main_footer{
display: flex;
justify-content: center;
align-items: center;
border-top: 5px solid #999b84;
width: 100%;
height: 120px;
background-color:#efd9d1;  
}


</style>



<script>
import { ref } from 'vue';
import { useStore } from "vuex";
import { computed } from '@vue/runtime-core';
import { GetProducts } from "../services/user.services";
import { GetReversedProducts } from "../services/user.services";
import router from "../router/index";

export default {
  name: 'Home',
  setup(){
    const store = useStore();
    const BookingItems = computed(() =>store.getters.get_BookingItems)
    const IsLoggedIn = computed(() => store.getters.IsLoggedIn)
    GetProducts()

    const searchQuery = ref("");
    const resultQuery = computed(() =>{
      if(searchQuery.value !== ""){
      return BookingItems.value.filter((item)=>{
        return searchQuery.value.toLowerCase().split(' ').every(v => item.name.toLowerCase().includes(v))
      })
      }else{
        return BookingItems.value;
      }
    });

    const sortLowHigh = () =>{
      store.dispatch("sortLowHigh")
      router.push({name:"Home"})
    }

    const sortHighLow = () =>{
      store.dispatch("sortHighLow")
      router.push({name:"Home"})
    }

    const sortOldNew = () =>{
      GetProducts()
      router.push({name:"Home"})
    }

    const sortNewOld = () =>{
      GetReversedProducts()
      router.push({name:"Home"})
    }

    const toBooking = (item) =>{
      store.dispatch("set_currentItem",item)
      router.push({name:"Booking"})
    }

    


    return {
      BookingItems,
      IsLoggedIn,
      resultQuery,
      searchQuery,
      sortLowHigh,
      sortHighLow,
      sortOldNew,
      sortNewOld,
      toBooking
    }
  }




};
</script>