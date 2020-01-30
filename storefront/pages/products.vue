<template>
  <div>
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
          <a :href="getLink(props.row.id)" target="_blank" class="is-small button is-link is-light">
            <b-icon size="is-normal" icon="open-in-new"></b-icon>
          </a>
          </div>
        </b-table-column>
      </template>
    </b-table>
    <br />
  </div>
</template>


<script>
import axios from "axios";

export default {
  data() {
    return {
      products: [],
      loading: true,

      columns: [
        {
          field: "variants[0]",
          label: "SKU",
          searchable: true
        },
        {
          field: "title",
          label: "Title",
          searchable: true
        },
        {
          field: "product_type",
          label: "Type",
          searchable: true
        },
        {
          field: "variants[0].inventory_quantity",
          label: "Qty",
          searchable: true
        }
      ]
    };
  },
  mounted() {
    let self = this;
    axios.get("http://localhost:5000/get/products").then(function(response) {
      self.products = response.data.products;
      self.loading = false;
    });
  },
  methods: {
    getLink(id){
      return "https://highoncarbs.myshopify.com/admin/products/"+String(id)
    }
  }
};
</script>