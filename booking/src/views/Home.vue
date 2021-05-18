<template>
  <div class="main">
    
    <div class="Product_container">
      <article>
        <img alt="SaloShoes" src="../assets/Salomon.jpeg" width="400" height="500"/>
        <h3>Gold Diamond Ring <span>16000$</span></h3>
        <br>
        <p>A symbol of the world’s greatest love stories for over 130 years.</p>
      </article>
      <article>
        <img alt="Berghans" src="../assets/Berghans.jpeg" width="400" height="500"/>
        <h3>Gold Diamond Ring <span>16000$</span></h3>
        <br>
        <p>A symbol of the world’s greatest love stories for over 130 years.</p>
      </article>
      <article>
        <img alt="Sovepose" src="../assets/sovepose.jpeg" width="400" height="500"/>
        <h3>Gold Diamond Ring <span>16000$</span></h3>
        <br>
        <p>A symbol of the world’s greatest love stories for over 130 years.</p>
      </article>
      <article>
        <img alt="Frostsko" src="../assets/frostsko.jpeg" width="400" height="500"/>
        <h2>Gold Diamond Ring<span>16000$</span></h2>
        <br>
        <p>A symbol of the world’s greatest love stories for over 130 years.</p>
      </article>
    </div>
    
  </div>
</template>



<style scoped>
article {
    border: 0.5px solid black;
    padding: 5px;
    font-size: 0.4em;
}

.Product_container {
    display: flex;
    width: 100%;
    flex-wrap: wrap;
    justify-content: space-around;
}


</style>


