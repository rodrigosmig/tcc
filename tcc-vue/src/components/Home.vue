<template>
    <div>
      <div class="input-group mb-3 termo-busca">
        <input type="text" class="form-control" v-model="search" placeholder="Digite o termo de busca" aria-label="Digite o termo de busca" required>
        <div class="input-group-append">
            <!-- <router-link :to="{ name: 'Classificados', params: { id: 1234 } }"> -->
              <button class="btn btn-outline-secondary" @click="collect_tweets" type="submit" title="buscar">
                <i class="fas fa-search"></i>
              </button>
            <!-- </router-link> -->
        </div>
      </div>
      <div v-if="display" class="alert alert-danger" role="alert">
        Digite algum termo para a busca.
      </div>
    </div>
    
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'Home',
    data () {
      return {
        search: '',
        display: false
      }
    },
    methods: {
      collect_tweets: function() {
          if(this.search == "") {
            this.display = true;
          }
          else {
            this.$router.push({
              name:'Classificados',
              params: {
                search_id: this.search
              }, 
              query: {
                display: true
              }
            })
          }
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.alert {
  text-align: center;
}

.termo-busca {
    width: 40%;
    height: 60px;
    margin-right: auto;
    margin-left: auto;
}

.termo-busca input, .termo-busca button {
    border-radius: 25px;
    margin-top: 140px;
}

.termo-busca button {
    font-size: 30px;
}
</style>
