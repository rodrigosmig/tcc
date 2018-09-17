<template>
  <div class="content">
    <b-table :items="searchs" :fields="fields">
    <template slot="show_details" slot-scope="tweet">
      <b-button size="sm" @click.stop="tweet.toggleDetails" @click="getTweets(tweet.item.id)" class="mr-2">
       {{ tweet.detailsShowing ? 'Hide' : 'Show'}} Details
      </b-button>
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
      </b-card>
    </template>
  </b-table>

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
</script>

<style>
  .content {
    width: 60%;
    margin-top: 70px;
    margin-left: auto;
    margin-right: auto;
  }
</style>
