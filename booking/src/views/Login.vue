<template>
  <div class="about">
    <h1>Please login</h1>

    <form @submit.prevent="submit">
      <div class="form-group">
        <label for="username">username</label>
        <input type="text" class="form-control" placeholder="Enter username"
        v-model = "username"
        >
      </div>

      <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control" placeholder="password"
        v-model = "password"
        >
      </div>
      <button type="submit" class="btn btn-primary">submit</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { Login } from "../services/user.services"

export default {
name: 'Login', 

setup() {
  const username = ref("");
  const password = ref("");


  const submit = () => {
    Login({username: username.value, 
            password: password.value})
    }
    return {
        username,
        password,
        submit
    }
}
};
</script>