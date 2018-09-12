<template>
    <div>
        <br><br><br><br>
        
        <div class="content col-md-6">
            <div v-show="loading" id="loading">
                <i class="fa fa-spinner fa-pulse fa-3x fa-fw" ></i>
                <span>...coletando tweets</span>
            </div>
            <!-- só exibira a div se uma pesquisa for realizada -->
            <div v-if="display" class="panel panel-info">
                                
                <div class="panel-heading">
                    <h4 class="media-heading">Media heading</h4>
                </div>

                <div class="media-body">
                    <p>Classificação: <strong>Positiva</strong></p>
                    <span class="user">@Usuário</span>
                    <div class="tweet">Dolorem aspernatur rerum, iure? Culpa iste aperiam sequi, fuga, quasi rerum, eum, quo natus tenetur officia placeat.</div>
                    <div class="correcao">Corrigir classificação:</div>
                    <ul class="nav">
                        <li class="nav-item">
                            <a class="nav-link active" href="#"><i class="fas fa-thumbs-up"></i></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"><i class="fas fa-thumbs-down"></i></a>
                        </li>
                    </ul>
                </div>

                <div class="media-body">
                    <p>Classificação: <strong>Positiva</strong></p>
                    <span class="user">@Usuário</span>
                    <div class="tweet">Dolorem aspernatur rerum, iure? Culpa iste aperiam sequi, fuga, quasi rerum, eum, quo natus tenetur officia placeat.</div>
                    <div class="correcao">Corrigir classificação:</div>
                    <ul class="nav">
                        <li class="nav-item">
                            <a class="nav-link active" href="#"><i class="fas fa-thumbs-up"></i></a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#"><i class="fas fa-thumbs-down"></i></a>
                        </li>
                    </ul>
                </div>

            </div>

            <div v-else>
                <div class="alert alert-danger" role="alert">
                    <strong>Ops!</strong> É preciso realizar uma busca para coletar e classificar os tweets.
                </div>
                <router-link :to="{ name: 'Home'}">
                    <button class="btn btn-primary" type="submit">Voltar</button>
                </router-link>
                
            </div>
            
        </div>
    </div>
    
</template>

<script>
    export default {
        name: 'Classificados',
        created() {
            this.search = this.$route.params.search_id;
            if(this.$route.query.display) {
                const url = "http://localhost:8000/tweets/?search=" + this.search
                this.loading = true;
                /* axios.get(url).then(tweets => {
                    console.log(tweets.data);                
                }) */
                this.display = this.$route.query.display;
            }
            this.loading = false;
        },
        data () {
            return {
                display : false,
                search: "",
                loading: false
        }
    },
        methods: {
            collect_tweets: function() {
          
            }
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    #loading span {
        font-size: 35px;
    }

    #loading {
        text-align: center
    }
    .content {
        margin-left: auto;
        margin-right: auto;
    }

    .media-body {
        background-color: white;
        padding-top: 10px;
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
        color: red;
    }
</style>
