<template>
    <div class="container form-container">
    <form @submit.prevent="submit" class="my-form shadow">
      <div class="form-group">
        <label for="firstname">First Name</label>
        <input type="text" class="form-control" placeholder="Enter your FirstName"
        v-model="firstname"
        >
      </div>
      <div class="form-group">
        <label for="lastname">Last Name</label>
        <input type="text" class="form-control" placeholder="Enter your LastName"
        v-model="lastname"
        >
      </div>
      <div class="form-group">
        <label for="Email">Email</label>
        <input type="email" class="form-control" placeholder="Enter your Email"
        v-model="email"
        >
      </div>
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" class="form-control" placeholder="Enter username"
        v-model="username"
        >
      </div>
      <div class="form-group">
        <label>Password</label>
        <input type="password" class="form-control" placeholder="Password"
        v-model="password"
        >
      </div>
      <button type="submit" class="btn btn-primary my-submit">Submit</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue';
import { Register } from "../services/user.services"

export default {
name: 'Register', 

setup() {
  const username = ref("");
  const password = ref("");
  const firstname = ref("");
  const lastname = ref("");
  const email = ref("");

  const submit = () => {
    Register({firstname: firstname.value,
            lastname: lastname.value,
            email: email.value, 
            username: username.value, 
            password: password.value})
    }
    return {
        firstname, 
        lastname, 
        email,
        username,
        password,
        submit
    }
}
};
</script>
