<template>
  <div class="columns is-marginless">
    <div class="column is-3 is-paddingless">
      <div class="hero has-background-myred is-fullheight">
        <div class="hero-head mt-6 mb-0 pb-0 mx-6">
          <figure class="image">
            <img src="~static/storefront-mono-white.svg" style="width:70px; height: auto ;" alt class="image" />
          </figure>
          <!-- <p class="tag is-light mt-3 has-text-weight-bold">OPEN SOURCE</p> -->
        </div>
        <div class="hero-body ml-5">
          <div>
            <p class="has-text-white">
              <!-- <span class="is-size-2 has-text-weight-semibold">👋</span> -->
              <br />
              <br />
              <span class="is-size-4">
                Before we start with your store
                <br />we need a few quick details.
              </span>
              <br />
              <br />
              <!-- <span class="has-text-weight-medium">
                    
                    1. Your store address</span>
              <br />
              <br />
                <span class="has-text-weight-medium">2.  Shopify API Keys</span>
              <br />
              <br />
                <span class="has-text-weight-medium">3.  Some Configuration</span>
              <br />-->
            </p>
          </div>
        </div>
        <div class="hero-foot footer-pattern"></div>
      </div>
    </div>
    <div class="column">
      <div class="section px-6">
        <div class>
          <b-tabs position="is-centered" v-model="activeTab">
            <b-tab-item icon="numeric-1-circle" label="Select Store">
              <div class="mt-6 pt-6 px-6 mx-6">
                <b-field label="Enter Shop URL">
                  <b-input icon="store" placeholder="myshop.shopify.com"></b-input>
                </b-field>
                <button class="is-pulled-right button is-black">Next</button>
              </div>
            </b-tab-item>

            <b-tab-item icon="numeric-2-circle" label="Set API"></b-tab-item>
            <b-tab-item icon="numeric-3-circle" label="Configure Defalts"></b-tab-item>
          </b-tabs>
        </div>
      </div>
      <div class="has-text-centered">
        <button class="button is-text is-centered has-text-link" style="text-decoration:underline">
          <b-icon icon="help-circle"></b-icon>
          <span>Need help setting things up? Contact Us</span>
        </button>
      </div>
    </div>
  </div>
  <!-- <section class="section">
  </section>-->
</template>

<script>
export default {
  layout: "empty",
  data() {
    return {
      activeTab: 0
    };
  }
};
</script>

<style>
.has-background-myred {
  background-color: #e38181;
}

.footer-pattern {
  /* / */
  background: transparent
    linear-gradient(0deg, rgba(255, 255, 255, 0.3), rgba(225, 225, 225, 0));

  /* background-color: rgba(255,255,255,.3); */
  /* This fixed height is only for demo, your use cases might not need it */
  height: 250px;
  --svg: url(~static/bank-note.svg);
  -webkit-mask-image: var(--svg);
  mask-image: var(--svg);
  fill: #eee;
  /* background-image: url(~static/pie-factory.svg); */
}
</style>