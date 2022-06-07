<template>
  <div>
    <div class="level" v-if="products != null">
      <div class="level-left">
        <div class="level-item">
          <p class="tag is-medium is-info is-light">
            <b-icon icon="check-decagram"></b-icon>
            <span>{{ products.length }} Products
              </span> </p>
        </div>
      </div>
    </div>
    <div v-if="products == null" class="has-text-centered" style="margin-top: 8rem">
      <b-icon icon="file-remove" size="is-large" class="has-text-grey-light"></b-icon>
      <br>
      <br>
      <p class="has-text-weight-bold has-text-dark is-size-5">Unable to load Products</p>
      <br />
      <p>
        Might be due to
        <span class="tag is-info">SHOP URL</span>
        &
        <span class="tag is-info">SHOP NAME</span>
        not set up.
      </p>
      <br />
      <button class="button">
        <b-icon icon="settings" class="icon-btn"></b-icon>Settings
      </button>
    </div>
    <div v-if="products != null">
      <b-table :data="products" :loading="loading">
        <template slot-scope="props">
          <b-table-column field="SKU" label="SKU" sortable>
            <span class="has-text-grey-light" v-if="props.row.variants[0].sku == ''">None</span>
            {{ props.row.variants[0].sku }}
          </b-table-column>
          <b-table-column field="Title" label="Title" sortable>{{ props.row.title }}</b-table-column>
          <b-table-column field="Type" label="Type" sortable>{{ props.row.product_type }}</b-table-column>
          <b-table-column field="Qty" label="Qty" sortable>
            <span
              class="tag is-info is-light has-text-weight-bold is-normal"
              :class="{ 'is-danger' :props.row.variants[0].inventory_quantity < 5  }"
            >{{ props.row.variants[0].inventory_quantity }}</span>
          </b-table-column>
          <b-table-column field="Action" label="Action">
            <div class="buttons">
              <button class="is-small button is-light">
                <b-icon size="is-normal" icon="eye-outline"></b-icon>
              </button>
              <a
                :href="getLink(props.row.id)"
                target="_blank"
                class="is-small button is-link is-light"
              >
                <b-icon size="is-normal" icon="open-in-new"></b-icon>
              </a>
            </div>
          </b-table-column>
        </template>
      </b-table>
    </div>
    <br />
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [],
      loading: true
    };
  },
  mounted() {
    let self = this;
    this.$axios.get("/get/products").then(function(response) {
      console.log(response.data.success)
      if (response.data.success) {
        self.products = response.data.data.products;
        self.loading = false;
        self.$buefy.snackbar.open({
          duration: 4000,
          message: response.data.success,
          type: "is-light",
          position: "is-top-right",
          actionText: "Close",
          queue: true,
          onAction: () => {
            self.isActive = false;
          }
        });
      }
      else {
        self.products = null;
        self.loading = false;
        self.$buefy.snackbar.open({
          duration: 4000,
          message: response.data.message,
          type: "is-light",
          position: "is-top-right",
          actionText: "Close",
          queue: true,
          onAction: () => {
            self.isActive = false;
          }
        });
      }
    });
  },
  methods: {
    getLink(id) {
      return "https://highoncarbs.myshopify.com/admin/products/" + String(id);
    }
  }
};
</script>