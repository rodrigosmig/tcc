<template>
  <div>
    <b-navbar toggleable="md" type="dark" variant="muted" fixed="top">
      <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>
      <b-navbar-brand href="#">
        <b-link :to="{ name: 'Home'}">Home</b-link>
      </b-navbar-brand>
      <b-collapse is-nav id="nav_collapse">

        <b-navbar-nav class="ml-auto">
          <b-nav-item type="submit" v-b-tooltip.hover title="Buscas cadastradas">
            <b-link :to="{ name: 'Buscas'}">Buscas</b-link>
          </b-nav-item>          
          <b-nav-item href="#">Contato</b-nav-item>
          <b-nav-item href="#">Sobre</b-nav-item>
        </b-navbar-nav>

      </b-collapse>
    </b-navbar>
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  /* body:before {
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
  } */
  .navbar {
    background: rgba(0, 0, 0, 1);
  }
  a, a:hover {
    text-decoration: none;
    color: inherit
  }
</style>
