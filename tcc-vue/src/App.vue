<template>
  <div id="app">
    <nav class="navbar fixed-top">
        <a class="navbar-brand" href="#">Logo</a>
        <ul class="nav justify-content-end">
            <li class="nav-item">
                <a class="nav-link active" href="#">Contato</a>
            </li>
            <li class="nav-item">
                <a class="nav-link" href="#">Sobre</a>
            </li>
        </ul>
    </nav>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  body:before {
    content: '';
    position: fixed;
    width: 100vw;
    height: 100vh;
    background-image: url("assets/background.jpg");
      background-position: center center;
      background-repeat: no-repeat;
      background-size: cover;
      -webkit-filter: blur(3px);
      -moz-filter: blur(3px);
      -o-filter: blur(3px);
      -ms-filter: blur(3px);
      filter: blur(3px);
  }
  .navbar {
    background: rgba(0, 0, 0, 0.3);
  }
</style>
