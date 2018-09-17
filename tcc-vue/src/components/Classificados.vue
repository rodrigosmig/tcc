<template>

    <div>
        <div class="content col-md-6">
            <div v-show="loading" id="loading">
                <i class="fa fa-spinner fa-pulse fa-3x fa-fw" ></i>
                <span>...coletando tweets</span>
            </div>
            <!-- só exibira a div se uma pesquisa for realizada -->
            <div v-if="display && search != null" class="panel panel-info">
                                
                <div class="panel-heading">
                    <h4 class="media-heading">Busca: <strong>{{search}}</strong></h4>
                </div>

                <div v-for="(tweet, index) in tweets" :key="tweet.id" class="media-body">
                    <p>
                        <span v-if="tweet.classification == 1">
                            Classificação: <strong style="color: blue">Positiva</strong>
                        </span>
                        <span v-else>
                            Classificação: <strong style="color: red">Negativa</strong>
                        </span>
                    </p>
                    <span class="user">@{{tweet.user}}</span>
                    <div class="tweet">{{tweet.tweet_text}}</div>
                    <div class="correcao">Corrigir classificação:</div>
                    <ul class="nav">
                        <li v-if="tweet.classification == 1" class="nav-item">
                            <span class="nav-link"><i class="fas fa-thumbs-up" style="color: blue"></i></span>
                        </li>
                        <li v-else class="nav-item">
                            <a @click="toPositive(index, tweet.id)" class="nav-link" href="javascript:void(0)"><i class="fas fa-thumbs-up" style="color: blue"></i></a>
                        </li>
                        <li v-if="tweet.classification == 0" class="nav-item">
                            <span class="nav-link"><i class="fas fa-thumbs-down" style="color: red"></i></span>
                        </li>
                        <li v-else class="nav-item">
                            <a @click="toNegative(index, tweet.id)" class="nav-link" href="javascript:void(0)"><i class="fas fa-thumbs-down" style="color: red"></i></a>
                        </li>
                    </ul>
                </div>

            </div>

            <div v-else>
                <b-alert show variant="danger"><strong>Ops!</strong> É preciso realizar uma busca para coletar e classificar os tweets.</b-alert>
                <router-link :to="{ name: 'Home'}">
                    <button class="btn btn-primary" type="submit">Voltar</button>
                </router-link>
                
            </div>
            
        </div>
    </div>

</template>

<script>
    import axios from 'axios'

    export default {
        name: 'Classificados',
        created() {
            this.search = this.$route.params.search_id;
            if(this.$route.query.display && this.search != "") {           
                this.loading = true;
                axios.get(this.url + "?search=" + this.search).then(tweets => {
                    this.tweets = tweets.data;
                    this.loading = false;              
                })
                this.display = this.$route.query.display;
            }           
        },
        data () {
            return {
                display : false,
                search: null,
                loading: false,
                tweets: [],
                url: "http://localhost:8000/tweets/"
        }
    },
        methods: {
            toPositive: function(index, id) {
                axios.patch(this.url + id + "/", {"classification": 1}).then(response => {
                    let change = this.tweets[index]
                    change.classification = "1"
                    this.tweets.splice(index, 1, change)              
                }).catch(error => {
                    alert("Classificação não alterada. Tente novamente.")
                })
            },
            toNegative: function(index, id) {
                axios.patch(this.url + id + "/", {"classification": 0}).then(response => {
                    console.log(response)
                    let change = this.tweets[index]
                    change.classification = "0"
                    this.tweets.splice(index, 1, change)              
                }).catch(error => {
                    alert("Classificação não alterada. Tente novamente.")
                })
            }
        }
    }
</script>

<style scoped>

    ul li a:link, a:visited {
        text-decoration: none;
    }
    #loading span {
        font-size: 35px;
    }

    #loading {
        text-align: center
    }
    .content {
        margin-top: 70px;
        margin-left: auto;
        margin-right: auto;
    }

    .media-body {
        background-color: white;
        padding-top: 10px;
        padding-left: 5px;
        padding-right: 5px;
    }

    .panel-info {
        border: 1px grey solid;
    }

    div.panel-heading{
        padding: 10px;
        background-color: #d9edf7
    }
    
    .tweet {
        font-style: italic;
    }

    .user {
        font-weight: bolder;
    }

    .media-body {
        border: 1px lightgrey solid;
    }

    .correcao {
        padding-top: 10px;
        
    }
</style>
