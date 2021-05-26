import { API_URL } from "../config";
import router from "../router/index"
import store from "../store/index";


export function Register(userdata) {
    fetch(`${API_URL}/register`, {
        method:"POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userdata)
      }).then((res) => {
          if(res.status && res.status === 200) {
              console.log("Registred")
              router.push({name: "Login"})
          }else if(res.status && res.status === 400){
            console.log("Not Registred");
            router.push({name: "Register"})
            alert("Username Taken! Register again.");

          }
      })
}

export function Add(userdata){
  fetch(`${API_URL}/profile`, {
    method:"POST",
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(userdata)
  }).then((res) => {
      if(res.status && res.status === 200) {
          console.log("Product Added !");
          GetProducts()
          GetBookings()
      }
  })
}

export function BookProduct(info){
  fetch(`${API_URL}/booking`, {
    method:"POST",
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(info)
  }).then((res) => {
      if(res.status && res.status === 200) {
          console.log("Booked !");
          router.push("Profile")
      }else if(res.status && res.status === 400){
        console.log("Not Booked !");

      }
  })
}

export function RemoveProduct(productId) {
  fetch(`${API_URL}/remove/${productId}`, {
    method:"DELETE",
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
    //body: JSON.stringify(productId)
  }).then((res) => {
      if(res.status && res.status === 200) {
          store.dispatch("deleteProduct",productId)
          GetBookings()
          console.log("Product deleted!")

      }
  })
};



export function GetProducts() {
    fetch(`${API_URL}/products`, {
      method:"GET",
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      },
    }).then((res) => {
      if (res.ok) {
          return res.json()
      }
      throw new Error('Respons ikke ok');
    })
    .then((data) => {
      console.log(data)
      store.dispatch("addProduct",data)

    }).catch((e) => {
      console.error(e)
    })
}

export function GetBookings() {
  fetch(`${API_URL}/bookings`, {
    method:"GET",
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
  }).then((res) => {
    if (res.ok) {
        return res.json()
    }
    throw new Error('Respons ikke ok');
  })
  .then((data) => {
    console.log(data)
    store.dispatch("getBookings",data)

  }).catch((e) => {
    console.error(e)
  })
}


export function GetReversedProducts() {
  fetch(`${API_URL}/products`, {
    method:"GET",
    headers: {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    },
  }).then((res) => {
    if (res.ok) {
        return res.json()
    }
    throw new Error('Respons ikke ok');
  })
  .then((data) => {
    console.log(data)
    store.dispatch("addProductReversed",data)

  }).catch((e) => {
    console.error(e)
  })
}





export function Login(userdata) {
    fetch(`${API_URL}/login`, {
        method:"POST",
        headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
        },
        body: JSON.stringify(userdata)
      }).then((res) => {
        if (res.ok) {
            return res.json()
        }
        alert("Username or password incorrect. Try again!");
        throw new Error('Respons ikke ok');
      })
      .then((data) => {
        store.dispatch("login")
        store.dispatch("initUser", data)
        //GetProducts()
        router.push({name: "Profile"})

      }).catch((e) => {
        console.error(e)
      })
}

