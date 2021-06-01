<template>
  <div class="container">
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
      <div
        v-for="item in currentItem"
        :key="item"
        class="col border border-dark card"
        style="width: 18rem"
      >
        <img
          v-bind:src="require(`../assets/${item.productImg}`)"
          alt=""
          style="width: 18rem"
          class="card-img-top"
        />
        <div class="card-body">
          <h5 class="card-title">{{ item.name }}</h5>
          <p class="card-text">{{ item.description }}</p>
        </div>

        <ul class="list-group list-group-flush">
          <li class="list-group-item">Price: {{ item.price }}kr,-</li>
          <li class="list-group-item">
            Availability: {{ item.startdate }} - {{ item.enddate }}
          </li>

          <form @submit.prevent="submit">
            <p>Start date:</p>
            <input
              required
              class="col form-control"
              v-model="startdate"
              v-bind:min="`${item.startdate}`"
              v-bind:max="`${item.enddate}`"
              type="date"
              id="example-date-input"
            />
            <p>End date:</p>
            <input
              required
              class="form-control"
              v-model="enddate"
              v-bind:min="`${item.startdate}`"
              v-bind:max="`${item.enddate}`"
              type="date"
              id="example-date-input"
            />

            <br />
          </form>
          <button
            type="submit"
            @click="bookProduct(item.productId, item.name)"
            class="btn btn-primary"
          >
            Book
          </button>
        </ul>
      </div>
    </div>
  </div>
</template>

<style>


.left {
  text-align: initial;
}
</style>
<script>
import { useStore } from "vuex";
import { BookProduct } from "../services/user.services";
import { ref } from "vue";

export default {
  setup() {
    const store = useStore();
    const currentItem = store.getters.get_currentItem;
    const userInfo = store.getters.get_userInfo;
    const myUser = userInfo[0].username;
    const startdate = ref("");
    const enddate = ref("");

    // calls on function located in user.services.js by passing necessary data.
    const bookProduct = (productId, productname) => {
      const info = [
        productId,
        productname,
        myUser,
        startdate.value,
        enddate.value,
      ];
      BookProduct(info);
    };

    return {
      currentItem,
      bookProduct,
      startdate,
      enddate,
    };
  },
};
</script>
