import { API_URL } from "../config";
import router from "../router/index";
import store from "../store/index";


// All functions using POST method converts userinput and passes data to the backend(routes.py file) which then calls on functions handling the database.
// All functions using GET method retrieves data from the backend(routes.py file) which then calls on functions handling the database.
// If data retrieved from backend/database or data passed causes Errors, responses are returned.


// Passes userinput from register form to backend
export function Register(userdata) {
  fetch(`${API_URL}/register`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userdata),
  }).then((res) => {
    if (res.status && res.status === 200) {
      console.log("Registred");
      router.push({ name: "Login" });
    } else if (res.status && res.status === 400) {
      console.log("Not Registred");
      router.push({ name: "Register" });
      alert("Username/Email Taken! Register again.");
    }
  });
}

// Passes product-info from create add input from profile page.
export function Add(userdata) {
  fetch(`${API_URL}/profile`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(userdata),
  }).then((res) => {
    if (res.status && res.status === 200) {
      console.log("Product Added !");
      GetProducts(); 
      GetBookings();
    }
  });
}

// Passes booking-info from booking page.
export function BookProduct(info) {
  fetch(`${API_URL}/booking`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(info),
  }).then((res) => {
    if (res.status && res.status === 200) {
      console.log("Booked !");
      GetProducts();
      router.push("Profile");
    } else if (res.status && res.status === 400) {
      console.log("Not Booked !");
    }
  });
}

// Passes the productID of the item user wants to remove and calls on the DELETE method which updates the database.
export function RemoveProduct(productId) {
  fetch(`${API_URL}/remove/${productId}`, {
    method: "DELETE",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  }).then((res) => {
    if (res.status && res.status === 200) {
      store.dispatch("deleteProduct", productId);
      GetBookings();
      console.log("Product deleted!");
    }
  });
}
export function RemoveBooking(IDs) {
  fetch(`${API_URL}/removebooking`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(IDs)
  }).then((res) => {
    if (res.status && res.status === 200) {
      store.dispatch("deleteBooking", IDs[0], IDs[1]);
      GetProducts();
      GetBookings();
      router.push({ name: "Home" });
      console.log("Booking deleted!");
    }
  });
}

// Retrieves all products from database
export function GetProducts() {
  fetch(`${API_URL}/products`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      }
      throw new Error("Respons ikke ok");
    })
    .then((data) => {
      store.dispatch("addProduct", data);
    })
    .catch((e) => {
      console.error(e);
    });
}

// Retrieves all bookings made from database
export function GetBookings() {
  fetch(`${API_URL}/bookings`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      }
      throw new Error("Respons ikke ok");
    })
    .then((data) => {
      console.log(data);
      store.dispatch("getBookings", data);
    })
    .catch((e) => {
      console.error(e);
    });
}

// Retrieves all products in reversed order from database
export function GetReversedProducts() {
  fetch(`${API_URL}/products`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      }
      throw new Error("Respons ikke ok");
    })
    .then((data) => {
      console.log(data);
      store.dispatch("addProductReversed", data);
    })
    .catch((e) => {
      console.error(e);
    });
}

// Passes login-info from Login page for authentication. 
export function Login(userdata) {
  fetch(`${API_URL}/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify(userdata),
  })
    .then((res) => {
      if (res.ok) {
        return res.json();
      }
      alert("Username or password incorrect. Try again!");
      throw new Error("Respons ikke ok");
    })
    .then((data) => {
      store.dispatch("login");
      store.dispatch("initUser", data);
      store.dispatch("set_grid_state", true);
      GetProducts();
      GetBookings();

      router.push({ name: "Profile" });
    })
    .catch((e) => {
      console.error(e);
    });
}

// Updates the current users selection of sorting by passing the state to the backend (New-Old,Hig-Low, etc.)
export function update_SortState(info) {
  fetch(`${API_URL}/updatesort`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(info),
  }).then((res) => {
    if (res.status && res.status === 200) {
      console.log("Sort state updated!");
    } else if (res.status && res.status === 400) {
      console.log("Sort not updated !");
    }
  });
}
