import { createStore } from "vuex";


export default createStore({

  state: {
    BookingItems: [], //list of all products

    currentItem: [], //the users currently chosen item to book

    bookedItems: [], //list of all booked items

    bookedItemsID: [], //list of productIDs of all booked items

    loggedIn: false, //login state (true if a user is logged in)

    sort_state: "sortNewOld", //default sort state

    grid_state: true, //default display (Grid)

    // Userinfo of currently logged in user
    user: [
      { username: "", firstname: "", lastname: "", email: "", sort_state: "" },
    ],

    //today: Date().getFullYear()+'-'+(Date().getMonth()+1)+'-'+Date().getDate(),
  },

  mutations: {
    // sorts all elements in BookingItems from lowest to highest price
    sortLowHigh: (state) => {
      state.BookingItems.sort(function (a, b) {
        return a.price - b.price;
      });
    },

    // sorts all elements in BookingItems from highest price to lowest price
    sortHighLow: (state) => {
      state.BookingItems.sort(function (a, b) {
        return b.price - a.price;
      });
    },

    // updates currentItem info
    set_currentItem: (state, item) => {
      state.currentItem = [];
      state.currentItem.push(item);
      console.log(state.currentItem[0]);
    },

    // updates login and logout state
    login: (state) => {
      state.loggedIn = true;
    },
    logout: (state) => {
      state.loggedIn = false;
    },

    // updates userinfo to current logged in user
    initUser: (state, data) => {
      (state.user[0].username = data.username),
        (state.user[0].firstname = data.firstname),
        (state.user[0].lastname = data.lastname),
        (state.user[0].email = data.email),
        (state.user[0].sort_state = data.sort_state);
    },

    // Adds each item retrieved from products table in database to BookingItems list.
    addProduct: (state, productList) => {
      console.log(productList);
      state.BookingItems = [];
      productList.forEach((element) => {
        state.BookingItems.push(element);
      });
    },

    // Adds each item retrieved from bookings table in database to bookedItems list.
    getBookings: (state, bookings) => {
      state.bookedItems = [];
      bookings.forEach((element) => {
        state.bookedItems.push(element);
      });
    },

    // Adds each item retrieved from products table in database in reversed order to the BookingItems list.
    addProductReversed: (state, productList) => {
      productList.reverse();
      state.BookingItems = [];
      productList.forEach((element) => {
        state.BookingItems.push(element);
      });
    },

    // Removes deleted product from BookingItems list
    deleteProduct: (state, productId) => {
      const index = state.BookingItems.map((item) => item.productId).indexOf(
        productId
      );
      if (index > -1) {
        state.BookingItems.splice(index, 1);
      }
    },

    deleteBooking: (state, bookingId, productId) => {
      const index = state.bookedItems
        .map((item) => item.bookingId)
        .indexOf(bookingId);
      if (index > -1) {
        state.bookedItems.splice(index, 1);
      }
      const index2 = state.bookedItemsID
        .map((item) => item.productId)
        .indexOf(productId);
      if (index2 > -1) {
        state.bookedItemsID.splice(index2, 1);
      }
    },

    // Adds booked items productIds to the bookedItemsID list to disable  book button.
    diasbleBook: (state, productId) => {
      state.bookedItemsID.push(productId);
    },

    set_sort_state: (state, sortstate) => {
      state.sort_state = sortstate;
    },

    set_grid_state: (state, grid_state) => {
      state.grid_state = grid_state;
    },
  },

  //calls on mutations
  actions: {
    login: (context) => {
      context.commit("login");
    },
    logout: (context) => {
      context.commit("logout");
    },
    initUser: (context, data) => {
      context.commit("initUser", data);
    },

    addProduct: (context, data) => {
      context.commit("addProduct", data);
    },

    addProductReversed: (context, data) => {
      context.commit("addProductReversed", data);
    },

    deleteProduct: (context, productId) => {
      context.commit("deleteProduct", productId);
    },

    deleteBooking: (context, bookingId, productId) => {
      context.commit("deleteBooking", bookingId, productId);
    },

    sortLowHigh: (context) => {
      context.commit("sortLowHigh");
    },

    sortHighLow: (context) => {
      context.commit("sortHighLow");
    },

    sortNewOld: (context) => {
      context.commit("sortNewOld");
    },

    set_currentItem: (context, item) => {
      context.commit("set_currentItem", item);
    },

    getBookings: (context, data) => {
      context.commit("getBookings", data);
    },

    diasbleBook: (context, productid) => {
      context.commit("getBookings", productid);
    },

    set_sort_state: (context, data) => {
      context.commit("set_sort_state", data);
    },

    set_grid_state: (context, data) => {
      context.commit("set_grid_state", data);
    },
  },

  modules: {},

  // retrives variables in state
  getters: {
    get_BookingItems: (state) => {
      return state.BookingItems;
    },
    IsLoggedIn: (state) => {
      return state.loggedIn === true;
    },

    get_userInfo: (state) => {
      return state.user;
    },

    get_currentItem: (state) => {
      return state.currentItem;
    },

    get_bookedItems: (state) => {
      return state.bookedItems;
    },

    get_bookedIDs: (state) => {
      return state.bookedItemsID;
    },

    get_sort_state: (state) => {
      return state.sort_state;
    },

    get_grid_state: (state) => {
      return state.grid_state;
    },
  },
});
