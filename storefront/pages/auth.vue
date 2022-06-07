<template>
  <div>
    <section class="section hero is-fullheight ">
      <div class="hero-head has-text-centered ">
        <!-- Logo Case -->
         <figure class="image">
            <img src="~static/storefront-mono.svg" style="width:70px; height: auto ;" alt class="container" />
          </figure>
        <!-- <p class="is-size-3 has-text-grey-light has-text-weight-bold" style="">STOREFRONT</p> -->
      </div>
      <div class="hero-body">
        <div class="container has-text-black">
          <div class="columns is-centered">
            <div class="column is-one-quarter-desktop is-centered">
              <p
                class="is-size-4 has-text-weight-bold has-text-black has-text-centered"
              >Welcome back.</p>
              <div class="" style="margin-top:3rem;">
                <div class >
                  <b-field :type="{'is-danger': error.username}" label="Username">
                    <b-input v-model="username" icon="account" placeholder="Enter Username" />
                  </b-field>
                  <b-field :type="{'is-danger': error.password}" label="Password">
                    <b-input
                      type="password"
                      v-model="password"
                      icon="lock"
                      placeholder="Enter Password"
                    />
                  </b-field>

                  <div class="control">
                    <button
                      native-type="submit"
                      @click="login"
                      class="button is-black is-fullwidth"
                    >
                      <span>Log In</span>
                    </button>
                  </div>
                </div>
              </div>
              <br />
              <div class="has-text-centered">
                <p>
                Fast Product Uploads for your store.
                </p>
                <p>
                Create Invoices on the go - GST Complaiant
                </p>
                <a href>Contact for a license</a>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="hero-footer">
        <p class="heading has-text-centered">Product of Peplum Studio</p>
        <a class="heading has-text-centered" href="https://github.com/highoncarbs">@highoncabs ↗</a>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  layout: "empty",
  data() {
    return {
      username: "",
      password: "",
      error: {}
    };
  },
   mounted() {
    if (this.$auth.loggedIn) {
      this.$router.push("/");
    }
  },
  methods: {
    checkData() {
      this.error = {};
      if (this.username && this.password) {
        return true;
      }

      if (!this.username) {
        this.$set(this.error, "username", true);
      }
      if (!this.password) {
        this.$set(this.error, "password", true);
      }
    },
    login() {
      if (this.checkData()) {
        let formData = { username: this.username, password: this.password };
        this.$auth.loginWith("local", { data: formData })
        .then(response => {
            if (response.status == 200) {
              this.$router.push("/");
            }
        })
        // if(this.$auth.loggedIn)
        // {
        //   this.$router.
        // }
        // await this.$auth.loginWith('local' , { 'data' :formData })
      }
    }
  }
};
</script>

<style >
html {
  /* background-color: #eee; */
}

</style>