<template>
    <div>      
      <div class="input-group mb-3 termo-busca">
        <b-input-group >
          <b-form-input v-model="search" :state="error" type="text" placeholder="Digite o termo de busca"></b-form-input>
          <b-input-group-append>
            <b-button variant="outline-secondary" @click="collect_tweets" type="submit" title="buscar">
              <i class="fas fa-search"></i>
            </b-button>
          </b-input-group-append>
          <b-form-invalid-feedback id="inputLiveFeedback">
            <!-- This will only be shown if the preceeding input has an invalid state -->
            <span class="error">Digite no mínimo 3 letras.</span>
          </b-form-invalid-feedback>
        </b-input-group>

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
        error: null,
        name: ""
      }
    },
    methods: {
      collect_tweets: function() {
          if(this.search.length < 3) {
            this.error = false
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
  #inputLiveFeedback {
    margin-left: 5px
  }
  .error {
    font-weight: bolder;
    /* background-color: lightblue */
  }
.alert {
  text-align: center;
}

.termo-busca {
    width: 40%;
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

.termo-busca input {
    height: 60px;
}
</style>
