import { API_URL } from "../config";


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
          }
      })
}

export function Login(userdata) {
    fetch(`${API_URL}/login`, {
        method:"POST",
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userdata)
      }).then((res) => {
          if(res.status && res.status === 200) {
              console.log("Registred")
          }
      })
}