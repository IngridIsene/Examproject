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
              class="col form-control"
              v-model="startdate"
              v-bind:min="`${item.startdate}`"
              v-bind:max="`${item.enddate}`"
              type="date"
              id="example-date-input"
              required
            />
            <p>End date:</p>
            <input
              class="form-control"
              v-model="enddate"
              v-bind:min="`${item.startdate}`"
              :max="`${item.enddate}`"
              type="date"
              id="example-date-input"
              required
            />

            <br />
            <button type="submit" class="btn btn-primary">Book</button>
          </form>
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

    const submit = () => {
      if (enddate.value < startdate.value){
        alert("End-date cannot be before start-date! Please change dates.")
      }else{
        console.log("inside submit");
        const info = [
          currentItem[0].productId,
          currentItem[0].name,
          myUser,
          startdate.value,
          enddate.value,
        ];
        console.log(info);
        BookProduct(info);
      }
    };

    return {
      currentItem,
      startdate,
      enddate,
      submit,
    };
  },
};
</script>
