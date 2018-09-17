<template>
  <div class="content">
    <b-table :items="searchs" :fields="fields">
    <template slot="show_details" slot-scope="tweet">
      <!-- we use @click.stop here to prevent emitting of a 'row-clicked' event  -->
      <b-button size="sm" @click.stop="tweet.toggleDetails" @click="getTweets(tweet.item.id)" class="mr-2">
       {{ tweet.detailsShowing ? 'Hide' : 'Show'}} Details
      </b-button>
      <!-- In some circumstances you may need to use @click.native.stop instead -->
      <!-- As `row.showDetails` is one-way, we call the toggleDetails function on @change -->
    </template>
    <template slot="row-details" slot-scope="tweet">
      <b-card v-for="t in tweet_data" :key="t.id">
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Usuário:</b></b-col>
          <b-col>@{{ t.user }}</b-col>
        </b-row>
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Tweet:</b></b-col>
          <b-col>{{ t.tweet_text }}</b-col>
        </b-row>
        <b-row class="mb-2">
          <b-col sm="3" class="text-sm-right"><b>Classificação:</b></b-col>
          <b-col v-if="t.classification == 1">
            <i class="fas fa-thumbs-up" style="color: blue"></i>
          </b-col>
          <b-col v-else>
            <i class="fas fa-thumbs-down" style="color: red"></i>
          </b-col>
        </b-row>
        <!-- <b-button size="sm" @click="tweet.toggleDetails">Hide Details</b-button> -->
      </b-card>
    </template>
  </b-table>














    <!-- <b-table striped hover
      responsive
      :items="searchs"
      :current-page="currentPage"
      :per-page="perPage"
      :fields="fields"
      @filtered="onFiltered"
      >
    </b-table>
    
    <b-row>
      <b-col md="6" class="my-1">
        <b-pagination :total-rows="totalRows" :per-page="perPage" v-model="currentPage" class="my-0" />
      </b-col>
    </b-row> -->
    
    <!-- <div class="content col-md-6">
        <table>
        <thead>
            <th>Expreesão de busca</th>
            <th>Data</th>
        </thead>
        <tbody>
            <tr v-for="(s) in searchs" :key="s.id">
                <td>{{s.expression}}</td>
                <td>{{s.search_date | fallback}}</td>
            </tr>
        </tbody>
    </table>
    </div> -->
    
  </div>
</template>

<script>
  import axios from 'axios'
  import moment from 'moment'
  export default {
    created() {
      axios.get(this.url + "buscas/").then(response => {
        this.searchs = response.data;
        console.log(this.searchs)
      })
    },
    data () {
      return {
        fields: {
            expression: {
              sortable: false,
              label: 'Expressão'
            },
            search_date: {
              sortable: true,
              label: 'Data da Busca',
              formatter: (value, key, item) => {
                return moment(String(value)).format('MM/DD/YYYY hh:mm')
              }
            },
            show_details: {
              label: 'Tweets'
            }
          },
        /* items: [
          { isActive: true, age: 40, first_name: 'Dickerson', last_name: 'Macdonald' },
          { isActive: false, age: 21, first_name: 'Larsen', last_name: 'Shaw' },
          { isActive: false, age: 89, first_name: 'Geneva', last_name: 'Wilson', _showDetails: true },
          { isActive: true, age: 38, first_name: 'Jami', last_name: 'Carney' }
        ], */
        searchs: [],
        url: "http://localhost:8000/",
        tweet_data: []
      }
    },
    methods: {
      getTweets(id) {
        console.log(this.url + "tweets/?search_id=" + id)
        axios.get(this.url + "tweets/?search_id=" + id).then(response => {
          console.log(response.data)
          this.tweet_data = response.data
        })
      }
    }
  }
  /* export default {
    name: 'Buscas',
      created() {
        axios.get(this.url).then(response => {
          this.searchs = response.data;
          console.log(this.searchs)
        })
      },
      data () {
        return {
          fields: [ 'expression', 'search_date', 'Tweets' ],
          url: "http://localhost:8000/buscas/",
          searchs: [],
          fields: {
            expression: {
              sortable: false,
              label: 'Expressão'
            },
            search_date: {
              sortable: true,
              label: 'Data da Busca',
              formatter: (value, key, item) => {
                return moment(String(value)).format('MM/DD/YYYY hh:mm')
              }
            },
            tweets: {
              label: 'Tweets'
            }
          },
          currentPage: 1,
          perPage: 10,
          totalRows: "",
        }
      },
      filters: {
        fallback: function(date) {
          return moment(String(date)).format('MM/DD/YYYY hh:mm')
        }
      },
      methods: {
        onFiltered (filteredItems) {
          // Trigger pagination to update the number of buttons/pages due to filtering
          this.totalRows = filteredItems.length
          this.currentPage = 1
        },
        collect_tweets: function() {
          
        }
      }
  } */
</script>

<style>
  .content {
    width: 60%;
    margin-top: 70px;
    margin-left: auto;
    margin-right: auto;
  }
</style>
