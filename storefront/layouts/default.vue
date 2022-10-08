<template>
  <div class>
    <div
      class="level px-4 py-4 is-mobile is-hidden-desktop"
      style="border-bottom: 1px solid #dbdbdb"
    >
      <div class="level-left">
        <figure class="image mt-1">
          <img src="~static/storefront-mono.svg" alt="" />
        </figure>
      </div>
      <div class="level-right">
        <button class="button is-text" @click="openSidebar = !openSidebar">
          Menu
        </button>
      </div>
    </div>
    <b-sidebar
      type="is-white"
      fullheight
      fullwidth
      overlay
      right
      v-model="openSidebar"
    >
      <div
        class="level px-4 py-4 is-mobile is-hidden-desktop"
        style="border-bottom: 1px solid #dbdbdb"
      >
        <div class="level-left">
          <figure class="image mt-1">
            <img src="~static/storefront-mono.svg" alt="" />
          </figure>
        </div>
        <div class="level-right">
          <button class="button is-text" @click="openSidebar = !openSidebar">
            Close
          </button>
        </div>
      </div>
      <div class="sidebar-content-body pl-2 mx-0 pb-4">
        <header class="has-text-centered"></header>
        <section class="sidebar-content-main">
          <br />
          <div class="menu sticky is-fullheight px-0">
            <nuxt-link class="button-x" to="/">
              <div class="button-x is-fullwidth pl-5">
                <b-icon class="mr-3" icon="view-dashboard"></b-icon>
                <span>Dashboard</span>
              </div>
            </nuxt-link>
            <nuxt-link class="button-x" to="/master">
              <div class="button-x is-fullwidth pl-5">
                <b-icon class="mr-3" icon="layers"></b-icon>
                <span>Master</span>
              </div>
            </nuxt-link>
            <nuxt-link class="button-x" to="/new">
              <div class="button-x is-fullwidth pl-5">
                <b-icon class="mr-3" icon="image"></b-icon>
                <span>Add Product</span>
              </div>
            </nuxt-link>
            <nuxt-link class="button-x" to="/orders">
              <div class="button-x is-fullwidth pl-5">
                <b-icon class="mr-3" icon="file"></b-icon>
                <span>Orders</span>
              </div>
            </nuxt-link>
            <nuxt-link class="button-x" to="/settings">
              <div class="button-x is-fullwidth pl-5">
                <b-icon class="mr-3" icon="cog"></b-icon>
                <span>Settings</span>
              </div>
            </nuxt-link>
            <a @click="logout()" class="button-x">
              <div class="button-x is-fullwidth pl-5">
                <b-icon icon="exit-to-app" class="mr-2"></b-icon>
                <span>Logout</span>
              </div>
            </a>
          </div>
        </section>
        <footer style="bottom: 15px !important; position: fixed">
          <div
            class="notification mb-2 is-warning"
            v-if="$auth.user.shop_url == ''"
          >
            <div class="media">
              <div class="media-left my-2">
                <b-icon icon="alert-circle"></b-icon>
              </div>
              <div class="media-content">
                <p>Shopify not connected</p>
                <n-link to="/settings" class="heading">Go to settings ↗</n-link>
              </div>
            </div>
          </div>
        
        </footer>
      </div>
    </b-sidebar>
    <!-- Desktop Nav Layout -->
    <div class="columns">
      <div
        class="column is-hidden-touch is-2 mt-0 pt-0 mb-0 pb-0"
        style="border-right: 1px solid #dbdbdb"
      >
        <div class="sidebar-content-body pl-2 mx-0 pb-4">
          <header class="has-text-centered"></header>
          <section class="sidebar-content-main">
            <br />
            <div class="menu sticky is-fullheight px-0">
              <nuxt-link class="button-x" to="/">
                <div class="button-x is-fullwidth pl-5">
                  <b-icon class="mr-3" icon="view-dashboard"></b-icon>
                  <span>Dashboard</span>
                </div>
              </nuxt-link>
              <nuxt-link class="button-x" to="/basic_master">
                <div class="button-x is-fullwidth pl-5">
                  <b-icon class="mr-3" icon="layers-outline"></b-icon>
                  <span>Basic Master</span>
                </div>
              </nuxt-link>
              <nuxt-link class="button-x" to="/master">
                <div class="button-x is-fullwidth pl-5">
                  <b-icon class="mr-3" icon="layers"></b-icon>
                  <span>Master</span>
                </div>
              </nuxt-link>
              <nuxt-link class="button-x" to="/new">
                <div class="button-x is-fullwidth pl-5">
                  <b-icon class="mr-3" icon="image"></b-icon>
                  <span>Add Product</span>
                </div>
              </nuxt-link>
              <nuxt-link class="button-x" to="/orders">
                <div class="button-x is-fullwidth pl-5">
                  <b-icon class="mr-3" icon="file"></b-icon>
                  <span>Orders</span>
                </div>
              </nuxt-link>
              <nuxt-link class="button-x" to="/settings">
                <div class="button-x is-fullwidth pl-5">
                  <b-icon class="mr-3" icon="cog"></b-icon>
                  <span>Settings</span>
                </div>
              </nuxt-link>
              <a @click="logout()" class="button-x">
                <div class="button-x is-fullwidth pl-5">
                  <b-icon icon="exit-to-app" class="mr-2"></b-icon>
                  <span>Logout</span>
                </div>
              </a>
            </div>
          </section>
          <footer style="bottom: 15px !important; position: fixed">
            <div
              class="notification mb-2 is-warning"
              v-if="$auth.user.shop_url == ''"
            >
              <div class="media">
                <div class="media-left my-2">
                  <b-icon icon="alert-circle"></b-icon>
                </div>
                <div class="media-content">
                  <p>Shopify not connected</p>
                  <n-link to="/settings" class="heading"
                    >Go to settings ↗</n-link
                  >
                </div>
              </div>
            </div>
            <div class="notification mt-0 pr-6">
              <div class="media">
                <div class="media-left px-4">
                  <figure class="image mt-1">
                    <img src="~static/storefront-mono.svg" alt="" />
                  </figure>
                </div>
                <div class="media-content">
                  <p class="heading">Product of <br />Pepum studios</p>
                  <a class="heading" href="">@highoncarbs ↗</a>
                </div>
              </div>
            </div>
          </footer>
        </div>
      </div>
      <div class="column">
        <section class="section pt-5">
          <transition name="fade">
            <nuxt />
          </transition>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  middleware: ["auth-user"],
  watch: {
    $route(to, from) {
      this.openSidebar = false;
    },
  },
  data() {
    return {
      expandOnHover: false,
      mobile: "reduce",
      openSidebar: false,
      reduce: false,
    };
  },
  methods: {
    async logout() {
      await this.$auth.logout().then((response) => {
        this.$router.push("/auth");
      });
    },
  },
};
</script>
<style>
* {
  font-family: "Inter", "Open Sans", "Helvetica Neue", sans-serif !important;
}

hr {
  background-color: #dbdbdb;
  height: 1px;
}
html {
  scroll-behavior: smooth;
}

.sidebar-content-body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

.sidebar-content-main {
  flex: 1;
}

.button-x {
  color: #0a0a0a;
  font-weight: 600;
  width: 100%;

  cursor: pointer;
  justify-content: left;
  padding-bottom: calc(0.5em - 1px);

  padding-top: calc(0.5em - 1px);
  text-align: left;
  vertical-align: top;
  display: flex;
  white-space: nowrap;
  transition: 0.2s all ease-in;
}
.button-x-center {
  justify-content: center;
  text-align: center;
}
.button-x:hover {
  background-color: rgb(228, 228, 228);
  border-radius: 3px;
  color: #0a0a0a !important;
}

.sub-nav .button-x {
  padding: 10px 10px;
  font-weight: 300 !important;
}
.sub-nav .button-x:hover {
  font-weight: 300;
}

.menu-burger {
  cursor: pointer;
  display: block;
  height: 3.25rem;
  position: relative;
  width: 3.25rem;
  margin-left: auto;
  padding: 10px 10px 5px 0;
}

.is-family-monospace {
  font-family: "Roboto Mono";
  text-transform: uppercase;
}

.th-wrap {
  color: black;
  font-weight: 600;
}

.modal-content {
  overflow-y: auto !important;
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.5s;
}
.fade-enter,
.fade-leave-active {
  opacity: 0;
}
li {
  list-style: none;
}
</style>
