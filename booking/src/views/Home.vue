<template>
  <div>
    <div class="parallax"></div>
    <div class="container">
      <br />
      <form class="d-flex">
        <input
          class="form-control me-2"
          type="text"
          v-model="searchQuery"
          placeholder="Search for products by name"
          aria-label="Search"
          id="homesearch"
        />

        <div class="dropdown">
          <button
            class="btn btn-secondary dropdown-toggle"
            type="button"
            id="dropdownMenu2"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Sort By
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
            <li>
              <button @click="sortLowHigh" class="dropdown-item" type="button">
                Price (Low - High)
              </button>
            </li>
            <li>
              <button @click="sortHighLow" class="dropdown-item" type="button">
                Price (High - Low)
              </button>
            </li>
            <li>
              <button @click="sortOldNew" class="dropdown-item" type="button">
                Oldest to Newest Ads
              </button>
            </li>
            <li>
              <button @click="sortNewOld" class="dropdown-item" type="button">
                Newest to Oldest Ads
              </button>
            </li>
          </ul>
        </div>

        <div class="dropdown">
          <button
            class="btn btn-secondary dropdown-toggle"
            type="button"
            id="dropdownMenu2"
            data-bs-toggle="dropdown"
            aria-expanded="false"
          >
            Display As
          </button>
          <ul class="dropdown-menu" aria-labelledby="dropdownMenu2">
            <li>
              <button @click="showGrid" class="dropdown-item" type="button">
                Grid
              </button>
            </li>
            <li>
              <button @click="showList" class="dropdown-item" type="button">
                List
              </button>
            </li>
          </ul>
        </div>
        
      </form>

      <br />
      <div
        v-if="gridState"
        class="bookings row row-cols-2 row-cols-lg-3 g-2 g-lg-3"
      >
        <div class="col" v-for="item in resultQuery" :key="item">
          <div
            class="outer-border p-3 border bg-light element border border-dark"
          >
            <img v-bind:src="require(`../assets/${item.productImg}`)" alt="" />
            <br />
            <h3>{{ item.name }}</h3>
            <p>{{ item.description }}</p>
            <p>{{ item.price }} kr,-</p>

            <button
              v-if="!IsLoggedIn && item.booked == 0"
              @click="toLogin()"
              type="button"
              class="mybutton btn btn-primary"
            >
              Book
            </button>

            <button
              v-if="!IsLoggedIn && item.booked == 1"
              type="button"
              class="disable btn btn-primary"
              disabled
            >
              Not Available
            </button>

            <button
              v-if="IsLoggedIn && item.booked == 0 && item.username != username"
              @click="toBooking(item)"
              type="button"
              class="btn btn-primary"
            >
              Book
            </button>

            <button
              v-if="IsLoggedIn && item.booked == 1 && item.username != username"
              type="button"
              class="disable btn btn-primary"
              disabled
            >
              Not Available
            </button>

            <button
              v-if="IsLoggedIn && item.username == username"
              type="button"
              class="disable btn btn-primary"
              disabled
            >
              Your Ad
            </button>
          </div>
        </div>
      </div>

      <div v-if="!gridState">
        <div
          v-for="item in resultQuery"
          :key="item"
          class="row border border-dark outer-border"
        >
          <div class="col-sm-5">
            <img
              v-bind:src="require(`../assets/${item.productImg}`)"
              alt=""
              style="height: 150px; width: 150px"
            />
          </div>
          <div class="left col-sm-2">
            <h2>{{ item.name }}</h2>
            <p>{{ item.description }}</p>
            <p>{{ item.price }} kr,-</p>

            <button
              v-if="!IsLoggedIn && item.booked == 0"
              @click="toLogin()"
              type="button"
              class="mybutton btn btn-primary"
            >
              Book
            </button>

            <button
              v-if="!IsLoggedIn && item.booked == 1"
              type="button"
              class="disable btn btn-primary"
              disabled
            >
              Not Available
            </button>
            <button
              v-if="IsLoggedIn && item.booked == 0 && item.username != username"
              @click="toBooking(item)"
              type="button"
              class="btn btn-primary"
            >
              Book
            </button>
            <button
              v-if="IsLoggedIn && item.booked == 1 && item.username != username"
              type="button"
              class="disable btn btn-primary"
              disabled
            >
              Not Available
            </button>

            <button
              v-if="IsLoggedIn && item.username == username"
              type="button"
              class="disable btn btn-primary"
              disabled
            >
              Your Ad
            </button>
          </div>
        </div>
      </div>
    </div>

   
  </div>
</template>

<style>
.parallax {
  background-image: url("../assets/forsidebilde.jpeg");
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

img {
  width: 300px;
  height: 300px;
  max-width: 100%;
  max-height: 100%;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.outer-border {
  max-width: 100%;
  max-height: 100%;
  margin-top: 10px;
}

.btn {
  background-color: #e4d3cf;
  border-color: #62959c;
  color: black;
}

.disable:disabled {
  background-color: #62959c;
  border-color: #62959c;
  color: black;
}
#homesearch {
  width: 50%;
}

.left {
  text-align: initial;
}
</style>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { computed } from "@vue/runtime-core";
import { GetProducts } from "../services/user.services";
import { GetReversedProducts, getSortState } from "../services/user.services";
import { update_SortState, updateGridState } from "../services/user.services";
import router from "../router/index";

export default {
  name: "Home",

  //intial function
  setup() {
    
    //retrieves variables initialized in store/index.js with getters.
    const store = useStore();
    const BookingItems = computed(() => store.getters.get_BookingItems);
    const IsLoggedIn = computed(() => store.getters.IsLoggedIn);
    const gridState = computed(() => store.getters.get_grid_state);
    const bookedItemsID = computed(() => store.getters.get_bookedIDs);
    const username = store.getters.get_userInfo[0].username;
    const user_gridState = computed(() => store.getters.get_user_grid_state);
    console.log(user_gridState.value)

    GetReversedProducts();

    if (username == ""){
      store.dispatch("set_grid_state", true);
    }else{
      if (user_gridState.value == "grid"){
        console.log("home grid")
        store.dispatch("set_grid_state", true);
      }else{
        console.log("home list")
        store.dispatch("set_grid_state", false);
      }
    }


     //sort
    const sortLowHigh = () => {
      store.dispatch("sortLowHigh");
      const info = [username, "sortLowHigh"];
      update_SortState(info);
      getSortState(username)
      console.log("button sortLowHigh");
      router.push({ name: "Home" });
    };
    //sort
    const sortHighLow = () => {
      store.dispatch("sortHighLow");
      const info = [username, "sortHighLow"];
      update_SortState(info);
      getSortState(username)
      console.log("button sortHighLow");
      router.push({ name: "Home" });
    };
    //sort
    const sortOldNew = () => {
      GetProducts();
      const info = [username, "sortOldNew"];
      update_SortState(info);
      getSortState(username)
      console.log("button sortOldNew");
      router.push({ name: "Home" });
    };
    //sort
    const sortNewOld = () => {
      GetReversedProducts();
      const info = [username, "sortNewOld"];
      update_SortState(info);
      getSortState(username)
      console.log("button sortNewOld");
      router.push({ name: "Home" });
    };
    

    // Handles search-field and filters based on input
    const searchQuery = ref("");
    const resultQuery = computed(() => {
      if (searchQuery.value !== "") {
        return BookingItems.value.filter((item) => {
          return searchQuery.value
            .toLowerCase()
            .split(" ")
            .every((v) => item.name.toLowerCase().includes(v));
        });
      } else {
        return BookingItems.value;
      }
    });

   

    const toBooking = (item) => {
      store.dispatch("set_currentItem", item);
      router.push({ name: "Booking" });
    };

    const toLogin = () => {
      router.push({ name: "Login" });
    };

    const showGrid = () => {
      const info = [username,"grid"]
      updateGridState(info)
      store.dispatch("set_user_grid_state","grid")
      store.dispatch("set_grid_state", true);
      router.push({ name: "Home" });
    };
    const showList = () => {
      const info = [username,"list"]
      updateGridState(info)
      store.dispatch("set_user_grid_state","list")
      store.dispatch("set_grid_state", false);
      router.push({ name: "Home" });
    };

    

    
    

    

    

    return {
      BookingItems,
      IsLoggedIn,
      bookedItemsID,
      resultQuery,
      searchQuery,
      sortLowHigh,
      sortHighLow,
      sortOldNew,
      sortNewOld,
      toBooking,
      username,
      showGrid,
      showList,
      gridState,
      toLogin,
      user_gridState
      
      
      
      
      
    };

    
  },

  
};
</script>
