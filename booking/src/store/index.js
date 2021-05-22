import { createStore } from "vuex";

export default createStore({
  state: {
    BookingItems: [
      { name: "Bergans Jakke", description: "En rosa vindjakke. Den perfekte jakken for fjelltur.", img: "../assets/Berghans.jpeg" },
      { name: "Ski", description: "Rosa ski.", img: "../assets/k2ski.jpeg" },
      { name: "Sovepose", description: "Rosa sovepose.", img: "../assets/sovepose.jpeg" },
      { name: "Salomon", description: "Ringenes herre sko.", img: "../assets/Salomon.jpeg" },
      { name: "Frostsko", description: "Rosa ski.", img: "../assets/frostsko.png" },
    ],

    loggedIn: false,

    user: [{username: "", firstname: "", lastname: "", email: ""}]
  },

  mutations: {
    login: state => {
      state.loggedIn = true
    },
    logout: state => {
      state.loggedIn = false
    },
    initUser: (state,data) => {
      state.user[0].username = data.username,
      state.user[0].firstname = data.firstname,
      state.user[0].lastname = data.lastname,
      state.user[0].email = data.email

    }
  },

  //action kaller på mutaion
  actions: {
    login: context => {
      context.commit("login")
    },
    logout: context => {
      context.commit("logout")
    },
    initUser:(context, data) => {
      context.commit("initUser", data)
    }

  },

  modules: {},

  getters: {
    get_BookingItems: state =>{
      return state.BookingItems
    },
    IsLoggedIn: state => {
      return state.loggedIn === true
    },

    get_userInfo: state => {
      return state.user
    }

  },

});