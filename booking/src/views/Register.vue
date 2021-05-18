<template>
  <div class="container">
    
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

      <div class="form-group">
        <label>firstname</label>
        <input type="text" class="form-control" placeholder="Enter firstname"
        v-model = "firstname"
        >
      </div>

      <div class="form-group">
        <label>lastname</label>
        <input type="text" class="form-control" placeholder="Enter lastname"
        v-model = "lastname"
        >
      </div>

      <div class="form-group">
        <label>email</label>
        <input type="text" class="form-control" placeholder="Enter email"
        v-model = "email"
        >
      </div>
      <button type="submit" class="btn btn-primary">submit</button>
    </form>
  </div>
</template>

<script>
import { ref } from 'vue' 
export default {
name: 'Register', 

setup() {
  const username = ref("");
  const password = ref("");
  const firstname = ref("");
  const lastname = ref("");
  const email = ref("");

  const submit = () => {
      fetch("http://127.0.0.1:5000/api/register", {
          method:"POST",
          body: {
              firstname: firstname.value,
              lastname: lastname.value,
              email: email.value, 
              username: username.value, 
              password: password.value
            }
        }).then((res) => {
            if(res.status && res.status === 200) {
                console.log("Registred")
            }
        })
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
