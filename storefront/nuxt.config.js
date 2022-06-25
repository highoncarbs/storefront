
export default {
  mode: 'universal',
  /*
  ** Headers of the page
  */
  head: {
    title: process.env.npm_package_name || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: process.env.npm_package_description || '' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.png' },
      { rel: 'stylesheet', type: 'text/css', href: 'https://cdn.jsdelivr.net/npm/inter-ui@3.10.0/inter.min.css' },

    ]
  },
  /*
  ** Customize the progress-bar color
  */
  loading: { color: 'orange' },
  /*
  ** Global CSS
  */
  css: [
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    // { src: '~/plugins/feather', ssr: false }
  ],
  /*
  ** Nuxt.js dev-modules
  */
  buildModules: [
    // Doc: https://github.com/nuxt-community/eslint-module
  ],
  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://github.com/nuxt-community/modules/tree/master/packages/bulma
    // '@nuxtjs/bulma',
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/style-resources',
    ['nuxt-buefy', { css: true }],


  ],
  /*
  ** Axios module configuration
  ** See https://axios.nuxtjs.org/options
  */
  axios: {
    host: 'localhost',
    port: '8585',
  },
  server: {
    // host: '192.168.1.108',
    port: '8284',
  },

  auth: {
    cookie: {
      prefix: 'auth.',
      maxAge: 604800,
      options: {
        path: '/'
      }
    },
    strategies: {
      local: {
        redirect: {
          login: '/login',
          logout: '/login',
         
          home: '/'
      },
      
        endpoints: {
          login: { url: '/login', method: 'post', propertyName: 'token' },
          logout: { url: '/logout', method: 'delete' },
          user: { url: '/user', method: 'get', propertyName: 'user' }
        },
        // tokenRequired: true,
        // tokenType: '',
        // globalToken: true,
        // autoFetchUser: true
      }
    }
  },
  styleResources: {
    scss: [
      '~/assets/b-style.scss'
    ]
  },
  /*
  ** Build configuration
  */
  build: {
    postcss: {
      preset: {
        features: {
          customProperties: false
        }
      }
    },
    /*
    ** You can extend webpack config here
    */
    extend(config, ctx) {
    }
  },
  /*
  ** ENV Variabels for your SHOPIFY Access token 
 */
  env: {
  }
}
