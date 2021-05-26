import { createStore } from "vuex";

export default createStore({
  state: {
    /*
    BookingItems: [
      { productId: 9000, name: "Bergans Jakke", description: "Rosa vindjakke.", img: "Berghans.jpeg" },
      { productId: 9001,name: "Ski", description: "Rosa ski.", img: "k2ski.jpeg" },
      { productId: 9002,name: "Sovepose", description: "Rosa sovepose.", img: "sovepose.jpeg" },
      { productId: 9003,name: "Salomon", description: "Ringenes herre sko.", img: "Salomon.jpeg" },
      { productId: 9004,name: "Frostsko", description: "Rosa ski.", img: "frostsko.jpeg" },
    ],
    */
    BookingItems: [],

    currentItem: [],

    bookedItems:[],


    loggedIn: false,

    user: [{username: "", firstname: "", lastname: "", email: ""}]

  },

  mutations: {
    sortLowHigh: state => {
      // window.localStorage.setItem("sort", "lowHigh");
      state.BookingItems.sort(function(a,b){
        return a.price -b.price;
      })
    },

    sortHighLow: state => {
      state.BookingItems.sort(function(a,b){
        return b.price - a.price;
      })
    },

    sortNewOld: state => {
      state.BookingItems.reverse();
    },

    set_currentItem: (state,item) =>{
      state.currentItem = []
      state.currentItem.push(item);
      console.log(state.currentItem[0]);
    },

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

    },
    addProduct: (state, productList) => {
      console.log(productList);
      state.BookingItems = [];
      productList.forEach(element => {
        state.BookingItems.push(element);
      });
    },

    getBookings: (state, bookings) => {
      state.bookedItems = [];
      // const sort = window.localStorage.getItem("sort");
      bookings.forEach(element => {
        state.bookedItems.push(element);
      });
    },
    
    addProductReversed: (state, productList) => {
      productList.reverse();
      state.BookingItems = [];
      productList.forEach(element => {
        state.BookingItems.push(element);
      });
    },
    

    deleteProduct: (state, productId) => {

      const index = state.BookingItems
        .map((item) => item.productId)
        .indexOf(productId);
      if (index > -1) {
        state.BookingItems.splice(index, 1);
      }
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
    },

    addProduct:(context,data) => {
      context.commit("addProduct",data)
    },

    addProductReversed:(context,data) => {
      context.commit("addProductReversed",data)
    },

    deleteProduct: (context,productId) =>{
      context.commit("deleteProduct",productId)
    },

    sortLowHigh: context => {
      context.commit("sortLowHigh")
    },

    sortHighLow: context => {
      context.commit("sortHighLow")
    },
    
    sortNewOld: context => {
      context.commit("sortNewOld")
    },

    set_currentItem: (context,item) =>{
      context.commit("set_currentItem",item)
    },

    getBookings: (context,data) => {
      context.commit("getBookings",data)
    },




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
    },

    get_currentItem : state =>{
      return state.currentItem
    },

    get_bookedItems : state =>{
      return state.bookedItems
    }


  },

});