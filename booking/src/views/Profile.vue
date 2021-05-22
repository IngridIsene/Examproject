<template>

  <div class="container">
    <br>
    <br>
    <br>
    <br>


  <div class="row">
    <div class="col-sm-3">
      <div class="card" style="width: 250px;">
        <img src="../assets/profilpic.jpeg" style="height: 200px; width: 250px;" class="card-img-top" alt="...">
        <div v-for="info in userInfo" :key ="info" class="card-body">
          <p class="card-text">{{info.firstname}}  {{info.lastname}}</p>
        </div>
      </div>
    </div>

    <div class="col-sm-9">
      <div class="card" style="width: 60rem;">
        <div class="card-header"> 
          <h2>Profile Information</h2>
        </div>
        <ul v-for="info in userInfo" :key ="info" class="list-group list-group-flush">
          <li class="list-group-item">{{info.firstname}}</li>
          <li class="list-group-item">{{info.lastname}}</li>
          <li class="list-group-item">{{info.username}}</li>
          <li class="list-group-item">{{info.email}}</li>
        </ul>
      </div>
    </div>
  </div>

  <br>

  <div class="row">
      <div class="col border border-dark" >
        <h2> Your bookings </h2>
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Booking ID</th>
              <th scope="col">Item</th>
              <th scope="col">Rental Date</th>

            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">456829</th>
              <td>Bergans Jakke</td>
              <td>21.05 - 25.05</td>

            </tr>
            <tr>
              <th scope="row">824171</th>
              <td>Ski</td>
              <td>18.06 - 13.07</td>

            </tr>
            <tr>
              <th scope="row">678643</th>
              <td>Sovepose</td>
              <td>18.06 - 13.07</td>

            </tr>
          </tbody>
        </table>




      </div>


      <div class="col border border-dark" >
        <h2> Your Ads </h2>
        <table class="table">
          <thead class="thead-dark">
            <tr>
              <th scope="col">Ad ID</th>
              <th scope="col">Item</th>


            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">456829</th>
              <td>Bergans Jakke</td>


            </tr>
            <tr>
              <th scope="row">824171</th>
              <td>Ski</td>


            </tr>
            <tr>
              <th scope="row">678643</th>
              <td>Sovepose</td>


            </tr>
          </tbody>
        </table>
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
import { useStore } from "vuex";
export default {
  name:"Profile",
  setup() {
    const store = useStore();
    const userInfo = store.getters.get_userInfo;

    return {
      userInfo, 
    } 
  }
};
</script>
