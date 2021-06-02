<template>
  <div class="container">
    <br />
    <br />
    <br />
    <br />
    <div class="left">
      <button type="button" class="homeb btn btn-primary">
        <router-link to="/" class="nav-link activate" aria-current="page"
          >Back to home</router-link
        >
      </button>
    </div>

    <div class="row">
      <div class="col-sm-3 card" style="width: 250px">
          <img
            src="../assets/profilpic.jpeg"
            style="height: 200px; width: 250px"
            class="card-img-top"
            alt="..."
          />
          <div v-for="info in userInfo" :key="info" class="card-body">
            <p class="card-text">{{ info.firstname }} {{ info.lastname }}</p>
          </div>
      </div>

      <div class="col-sm-9 card" style="width: 60rem">
          <div class="card-header">
            <h2>Profile Information</h2>
          </div>
          <ul
            v-for="info in userInfo"
            :key="info"
            class="list-group list-group-flush"
          >
            <li class="list-group-item">{{ info.firstname }}</li>
            <li class="list-group-item">{{ info.lastname }}</li>
            <li class="list-group-item">{{ info.username }}</li>
            <li class="list-group-item">{{ info.email }}</li>
          </ul>
      </div>
    
      
    </div>
    <br />

    <div class="row">
      <div class="col border border-dark">
        <h2>Your bookings</h2>
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Booking ID</th>
              <th scope="col">Product ID</th>
              <th scope="col">Product Name</th>
              <th scope="col">Rented Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in bookedItems" :key="item">
              <th scope="row" v-if="item.username == username">
                {{ item.bookingId }}
              </th>
              <td v-if="item.username == username">{{ item.productId }}</td>
              <td v-if="item.username == username">{{ item.productname }}</td>
              <td v-if="item.username == username">
                {{ item.startdate }} - {{ item.enddate }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="col border border-dark">
        <h2>Your Ads</h2>
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Ad ID</th>
              <th scope="col">Item</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in BookingItems" :key="item">
              <th scope="row" v-if="item.username == username">
                {{ item.productId }}
              </th>
              <td v-if="item.username == username">{{ item.name }}</td>
              <td v-if="item.username == username">
                <button
                  @click="deleteProduct(item.productId)"
                  class="btn btn-light"
                >
                  X
                </button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <br />
    <br />

    <div class="row border border-dark">
      <div class="col-sm-3"></div>
      <div class="col-sm-6">
        <br />
        <h2>Create an Ad</h2>
        <br />
        <form @submit.prevent="submit">
          <div class="mb-3">
            <input
              class="form-control"
              type="text"
              placeholder="Product Name"
              aria-label="default input example"
              v-model="productname"
              required
            />
          </div>
          <div class="mb-3">
            <input
              class="form-control"
              type="number"
              placeholder="Price"
              aria-label="default input example"
              v-model="price"
              required
            />
          </div>
          <div class="mb-3">
            <input
              class="form-control"
              type="date"
              id="example-date-input"
              :min="today"
              v-model="start_date"
              required
            />
          </div>
          <div class="mb-3">
            <input
              class="form-control"
              type="date"
              id="example-date-input"
              :min="start_date"
              v-model="end_date"
              required
            />
          </div>
          <div class="mb-3">
            <label for="exampleFormControlTextarea1" class="form-label"
              >Product Description</label
            >
            <textarea
              class="form-control"
              id="exampleFormControlTextarea1"
              rows="3"
              v-model="description"
              required
            ></textarea>
          </div>

          <div class="mb-3">
            <select v-model="images" required>
              <option value="" disabled selected hidden>Choose an image</option>
              <option value="k2ski.jpeg">Ski</option>
              <option value="sovepose.jpeg">Sovepose</option>
              <option value="Berghans.jpeg">Jakke</option>
              <option value="frostsko.jpeg">Frostsko</option>
            </select>
          </div>

          <button
            type="submit"
            class="btn btn-primary"
          >
            Create Ad
          </button>
        </form>
        <br />
        <br />
        <br />
      </div>
    </div>
  </div>
</template>

<style scoped>
.img-thumbnail {
  margin: 10px;
  position: relative;
  margin-top: 50px;
}

.card {
  margin-top: 5px;
}
h1 {
  position: relative;
  margin-top: 10px;
}
</style>

<script>
import { ref } from "vue";
import { useStore } from "vuex";
import { Add, GetBookings } from "../services/user.services";
import { RemoveProduct } from "../services/user.services";
import { computed } from "@vue/runtime-core";

export default {
  name: "Profile",
  setup() {

    // initial variables from store/index.js
    const store = useStore();
    const userInfo = store.getters.get_userInfo;
    const productname = ref("");
    const price = ref("");
    const start_date = ref("");
    const end_date = ref("");
    const description = ref("");
    const images = ref("");
    const BookingItems = computed(() => store.getters.get_BookingItems);
    const username = userInfo[0].username;
    

    const deleteProduct = (productId) => {
      RemoveProduct(productId);
      console.log(productId);
    };

    GetBookings();
    const bookedItems = computed(() => store.getters.get_bookedItems);


    // Gets current date and adds missing leading zeros.
    const currentDate = () => {
      const current = new Date();
      let month = current.getMonth() + 1;
      let day = current.getDate();

      if (day < 10) {
        day = "0" + day.toString();
      }

      if (month < 10) {
        month = "0" + month.toString();
      }

      return `${current.getFullYear()}-${month}-${day}`;
  
    };
    const today = currentDate();

    // When form is submitted, the function Adds the product, updates the page and emties the input fields.
    const submit = () => {

      Add({
        username: store.getters.get_userInfo[0].username,
        productname: productname.value,
        price: price.value,
        start_date: start_date.value,
        end_date: end_date.value,
        description: description.value,
        productImg: images.value,
      });

      GetBookings();

      productname.value = "";
      price.value = "";
      start_date.value = "";
      end_date.value = "";
      description.value = "";
      images.value = "";
    };

    return {
      userInfo,
      productname,
      price,
      start_date,
      end_date,
      description,
      images,
      submit,
      BookingItems,
      username,
      deleteProduct,
      bookedItems,
      currentDate,
      today
    };
  },
};
</script>
