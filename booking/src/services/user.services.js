import { API_URL } from "../config";
import router from "../router/index"


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
          'Accept': 'application/json'
        },
        body: JSON.stringify(userdata)
      }).then((res) => {
        if (res.ok) {
            return res.json()
        }
        throw new Error('Respons ikke ok');
      })
      .then((data) => {
        router.push({name: "Home"})
        console.log(data)

      }).catch((e) => {
        console.error(e)
      })
}