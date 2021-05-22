<template>
  <div class="about">
    <h1 class="h3 mb-3 font-weight-normal">Please reigster</h1>
    <div class = "text-center">
      <form @submit.prevent="submit">

        <div class="form-group">
          <label for="firstname">First Name</label>
          <input type="text" class="form-control" placeholder="Enter firstname" required autofocus
          v-model = "firstname"
          >
        </div>

        <div class="form-group">
          <label for="lastname">Last Name</label>
          <input type="text" class="form-control" placeholder="Enter lastname" required autofocus
          v-model = "lastname"
          >
        </div>

        <div class="form-group">
          <label for="lastname">Email</label>
          <input type="email" class="form-control" placeholder="Enter email" required autofocus
          v-model = "email"
          >
        </div>

        <div class="form-group">
          <label for="username">Username</label>
          <input type="text" class="form-control" placeholder="Enter username" required autofocus
          v-model = "username"
          >
        </div>

        <div class="form-group">
          <label>Password</label>
          <input type="password" class="form-control" placeholder="password"
          v-model = "password"
          >
        </div>
        <button type="submit" class="btn btn-primary">Submit</button>
      </form>
      </div>
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
