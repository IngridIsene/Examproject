<template>
  <div id="nav">
    <nav class="navbar navbar-expand navbar-light bg-light fixed-top">
      <div class="container-fluid">
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <router-link to="/" class="nav-link active" aria-current="page"
                >Home</router-link
              >
            </li>

            <li class="nav-item" v-if="!IsLoggedIn">
              <router-link
                to="/login"
                class="nav-link active"
                aria-current="page"
                >Log in</router-link
              >
            </li>
            <li class="nav-item" v-if="!IsLoggedIn">
              <router-link
                to="/register"
                class="nav-link active"
                aria-current="page"
                >Register</router-link
              >
            </li>
            <li class="nav-item" v-if="IsLoggedIn">
              <router-link
                to="/profile"
                class="nav-link active"
                aria-current="page"
                >Profile</router-link
              >
            </li>

            <li class="nav-item" v-if="IsLoggedIn" @click="Logout">
              <router-link to="/" class="nav-link active" aria-current="page"
                >Logout</router-link
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <router-view />
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #8e9775;
}

#nav {
  padding: 1px;
  width: 100%;
}
</style>

<script>
import { useStore } from "vuex";
import { computed } from "@vue/runtime-core";
import { GetReversedProducts } from "./services/user.services";
import router from "./router/index";

export default {
  setup() {
    const store = useStore();
    const IsLoggedIn = computed(() => store.getters.IsLoggedIn);
    const BookingItems = computed(() => store.getters.get_BookingItems);

    const Logout = () => {
      store.dispatch("logout");
      GetReversedProducts();
      store.dispatch("set_grid_state", true);
      router.push({ name: "Home" });
    };

    return {
      IsLoggedIn,
      Logout,
      BookingItems,
    };
  },
};
</script>
