<template>
  <div class="section container">

   <transition name="fade">
          <div v-if="showSetup">
            <div class="level my-0">
              <div class="level-left">
                <div class="level-item">
                  <p class="is-size-5 has-text-weight-semibold">Dashboard</p>
                </div>
              </div>
              <div class="level-right">
                <div class="level-item">
                  <button class="button is-rounded" @click="showSetup = !showSetup">
                    <b-icon icon="help-circle" class="has-text-danger"></b-icon>
                    <span class="ml-2"> Show Setup </span>
                  </button>
                </div>
              </div>
            </div>
            <br />
          </div>
        </transition>
        <transition name="fade">
          <div class="columns" v-show="!showSetup">
            <div class="colum is-4">
              <div >
                <figure class="image is-64x64">
                <img  src="~/static/storefront-mono.svg" alt="" />
                </figure>
                <br>
                <div class="level my-0 mt-4">
                  <div class="level-left">
                    <div class="level-item">
                      <h1 class="title has-text-weight-black">
                        Setup your Storefront
                      </h1>
                    </div>
                  </div>
                  <div class="level-right">
                    <div class="level-item">
                      <button @click="showSetup = !showSetup" class="button is-text">
                        Hide
                      </button>
                    </div>
                  </div>
                </div>
                <ul>
                  <li @click="$router.push('/settings')" class="steps-btn">
                    <article class="media">
                      <div class="media-content">
                        <div class="content">
                          <span class="has-text-left has-text-weight-medium">
                            Set a Shopify API in settings<br />

                            <span class="has-text-grey has-text-weight-normal"
                              >Get the API key from Shopify Private Apps</span
                            >
                          </span>
                        </div>
                      </div>
                      <div class="media-right py-2">
                        <b-icon icon="arrow-top-right" class="ml-3"></b-icon>
                      </div>
                    </article>
                  </li>
                  <li
                    @click="$router.push('/settings')"
                    class="steps-btn"
                  >
                    <article class="media">
                      <div class="media-content">
                        <div class="content">
                          <span class="has-text-left has-text-weight-medium">
                            Add Company Logo for Invoice <br />

                            <span class="has-text-grey has-text-weight-normal"
                              >Address & Other Firm Details for Invoice</span
                            >
                          </span>
                        </div>
                      </div>
                      <div class="media-right py-2">
                        <b-icon icon="arrow-top-right" class="ml-3"></b-icon>
                      </div>
                    </article>
                    <a class="py-3 is-info"> </a>
                  </li>
                
                  <li
                    @click="$router.push('/admin/panel/admin')"
                    class="steps-btn has-background-warning-light"
                  >
                    <article class="media">
                      <div class="media-left py-3 px-0 mr-4">
                        <b-icon
                          icon="lock"
                          class="has-text-warning-dark"
                        ></b-icon>
                      </div>
                      <div class="media-content">
                        <div class="content">
                          <span
                            class="has-text-left has-text-warning-dark has-text-weight-medium"
                          >
                            Change your Admin Login and Password to make it
                            secure. <br />

                            <span
                              class="has-text-warning-dark has-text-weight-normal"
                              >Change Default username & Password</span
                            >
                          </span>
                        </div>
                      </div>
                      <div class="media-right py-2">
                        <b-icon
                          icon="arrow-top-right"
                          class="ml-3 has-text-warning-dark"
                        ></b-icon>
                      </div>
                    </article>
                    <a class="py-3 is-info"> </a>
                  </li>
                </ul>
              </div>
           
            </div>
          </div>
        </transition>
  </div>


</template>

<script>

export default {
 data(){
   return{
     showSetup: false,
   }
 }
}
</script>
<style scoped>

.welcome {
  background-image: linear-gradient(
    45deg,
    #ff9a9e 0%,
    #fad0c4 99%,
    #fad0c4 100%
  );
}
.steps-btn {
  border: 1.5px solid #eee;
  border-radius: 7px;
  padding: 0.75rem 1.5rem;
  margin: 1rem 0;
  cursor: pointer;
  transition: 0.2s all ease-in;
}
.steps-btn:hover {
  background-color: #fee;

  border: 1.5px solid #dbdbdb;
}
</style>
