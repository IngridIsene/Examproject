<template>
  <div class="about">

    <h1 class="h3 mb-3 font-weight-normal">Please login</h1>
      <form @submit.prevent="submit" class="outer-border text-center">
        <div class="form-group" style="margin-top:30px">
          <label for="username">Username</label>
          <input
            type="text"
            class="form-control"
            placeholder="Enter username"
            required
            autofocus
            v-model="username"
          />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input
            type="password"
            class="form-control"
            placeholder="password"
            v-model="password"
          />
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
  </div>
</template>

<style scoped>
.form-group {
  padding: 10px;
  margin: 10px;
}
form {
  width: 500px;
  height: 700px;
  margin: auto;
  position: relative;
}



</style>

<script>
import { ref } from "vue";
import { Login } from "../services/user.services";

export default {
  name: "Login",

  setup() {
    const username = ref("");
    const password = ref("");

    const submit = () => {
      Login({ username: username.value, password: password.value });

      username.value = "";
      password.value = "";
    };

    return {
      username,
      password,
      submit,
    };
  },
};
</script>
