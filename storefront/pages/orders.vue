<template>
  <div class>
    <div class="level">
      <div class="level-left">
        <p class="level-item">
          <span class="title is-size-4">Orders</span>
        </p>
        <div class="level-item" v-if="checkedRows != 0">
          <div class="buttons">
            <button class="button is-info">
              <b-icon icon="printer" class="mr-2"></b-icon>
              <span>Print Invoices</span>
            </button>
            <button @click="printImgChecked()" class="button is-success">
              <b-icon icon="image" class="mr-2"></b-icon>
              <span>Print Orders</span>
            </button>
            <!-- <b-select @input="getOrderList" icon="check" v-model="order_type">
              <option value="order">Order Placed</option>
              <option value="abandon">Abandoned Orders</option>
            </b-select> -->
          </div>
        </div>
      </div>
      <div class="level-right">
        <div class="level-item">
          <b-field>
            <b-select @input="getOrderList" icon="check" v-model="order_type">
              <option value="order">Order Placed</option>
              <option value="abandon">Abandoned Orders</option>
            </b-select>
          </b-field>
        </div>
      </div>
    </div>

    <b-table :checked-rows.sync="checkedRows"
                    checkable :data="orderlist">
      <b-table-column label="Order ID" v-slot="props">
        <span class="has-text-weight-bold">
          # {{ props.row.order_number }}
        </span>
      </b-table-column>
      <b-table-column label="Name" v-slot="props">
        <span v-if="props.row.shipping_address">
          {{
            props.row.shipping_address.first_name +
            " " +
            props.row.shipping_address.last_name
          }}
        </span>
      </b-table-column>
      <b-table-column label="Items" v-slot="props">
        <span class="tag is-link hsas-text-weight-semibold">
          {{ props.row.line_items.length }}
        </span>
      </b-table-column>
      <b-table-column label="Order Value" v-slot="props">
        <!-- <span class="tag is-link hsas-text-weight-semibold"> -->
        {{ props.row.currency + " " + props.row.current_subtotal_price }}
        <!-- </span> -->
      </b-table-column>
      <b-table-column label="Date" v-slot="props">
        <!-- <span class="tag is-link hsas-text-weight-semibold"> -->
        {{ new Date(props.row.created_at).toLocaleString("en-IN") }}
        <!-- </span> -->
      </b-table-column>

      <b-table-column label="Action" v-slot="props">
        <div class="buttons">
          <button class="button" @click="createInv(props.row)">Invoice</button>
          <button class="button is-link" @click="printImg(props.row)">
            <b-icon icon="file-image"></b-icon>
          </button>
       
          <button class="button is-success"  @click="printInv(props.row.order_number)">
<b-icon icon="printer"></b-icon>

          </button>
          <!-- <button class="button">
              <b-icon icon="dots"></b-icon>
              </button> -->
        </div>
      </b-table-column>
      <template #empty>
        <div class="has-text-centered">
          <b-icon
            icon="file"
            class="has-text-grey mt-6"
            size="is-large"
          ></b-icon>
          <br />
          <p class="is-size-5 has-text-grey has-text-weight-semibold">
            No records
          </p>
        </div>
      </template>
    </b-table>

    <b-modal @close="cleanCurrOrder()" v-model="showInv">
      <div class="box" v-if="currOrder">
        <div class="level is-mobile">
          <div class="level-left">
            <div class="level-item">
              <p class="title is-size-5">Create Invoice</p>
            </div>
          </div>
          <div class="level-right">
            <div class="level-item">
              <button class="button is-link" @click="csvOrder()">
                <div class="media is-size-6">
                  <b-icon class="media-left" icon="file-excel"></b-icon>
                  <div class="media-content">
                    <p>Download for Excel</p>
                  </div>
                </div>
              </button>
            </div>
          </div>
        </div>
        <b-field class="is-grouped">
          <b-field label="Order Type">
            <b-select v-model="inv.type">
              <option value="india">India</option>
              <option value="intra">Rajasthan</option>
              <option value="export">Export</option>
            </b-select>
          </b-field>
          <b-field label="Inv. Date">
            <b-datepicker append-to-body v-model="inv.date"></b-datepicker>
          </b-field>
          <b-field label="GST Brackets %">
            <div class="buttons">
              <button class="button" @click="setTax(5)">5</button>
              <button class="button" @click="setTax(9)">9</button>
              <button class="button" @click="setTax(12)">12</button>
              <button class="button" @click="setTax(18)">18</button>
              <button class="button is-light" @click="setTax(null)">
                Clear
              </button>
            </div>
          </b-field>
        </b-field>
        <b-field label="GST">
            <b-input v-model="inv.gst" placeholder="Enter Customer GST Numebr"></b-input>
        </b-field>
        <b-field label="Discount %">
          <div class="buttons">
            <button class="button" @click="setDis('10')">10</button>
            <button class="button" @click="setDis('15')">15</button>
            <button class="button" @click="setDis('20')">20</button>
            <button class="button" @click="setDis('25')">25</button>
            <button class="button is-light" @click="setDis(null)">Clear</button>
          </div>
        </b-field>
        <b-table :data="currOrder.line_items">
          <b-table-column v-slot="props" label="S.No">{{
            props.index + 1
          }}</b-table-column>
          <b-table-column v-slot="props" label="Image">
            <figure class="image is-96x96 has-background-light">
              <img :src="props.row.image" alt="" />
            </figure>
          </b-table-column>
          <b-table-column v-slot="props" label="Name">{{
            props.row.title
          }}</b-table-column>
          <b-table-column v-slot="props" label="Qty">{{
            props.row.quantity
          }}</b-table-column>
          <b-table-column v-slot="props" label="Price">{{
            props.row.price
          }}</b-table-column>
          <b-table-column v-slot="props" label="Discount %">
            <b-input v-model="props.row.discount" type="number"></b-input>
          </b-table-column>
          <b-table-column v-slot="props" label="GST %">
            <b-input v-model="props.row.tax" type="number"></b-input>
          </b-table-column>
          <template #footer> </template>
        </b-table>
        <br />
        <b-field class="is-grouped">
          <b-field label="Invoice No">
            <b-input
              v-model="inv.inv_num"
              placeholder="Invoice Number"
            ></b-input>
          </b-field>
          <b-field label="Shipping Rate">
            <b-input
              v-model="inv.shipping_rate"
              placeholder="Shipping Rate"
            ></b-input>
          </b-field>
          <b-field label="Shipping Tax">
            <b-input
              v-model="inv.shipping_tax"
              placeholder="Shipping Tax %"
            ></b-input>
          </b-field>
        </b-field>
        <hr />
        <div class="level">
          <div class="level-left">
            <div class="buttons">
              <button class="button is-link" @click="saveInv()">
                Save Invoice
              </button>
              <button
                class="button is-link is-light"
                @click="printInv(currOrder.order_number)"
              >
                Print Invoice
              </button>
            </div>
          </div>
          <div class="level-right">
            <span class="button is-text">
              <b-icon class="mr-3" icon="information"></b-icon>
              <span> Save Invoice before printing </span>
            </span>
          </div>
        </div>
      </div>
    </b-modal>
  </div>
</template>


<script>
export default {
  data() {
    return {
      inv: {
        date: null,
        gst: null,
        inv_num: null,
        type: "india",
        shipping_rate: null,
        shipping_tax: null,
      },
      order_img: [],
      checkedRows: [],

      orderlist: [],
      order_type: "order",
      showInv: false,
      showOrder: false,
      currOrder: null,
      shopurl: this.$auth.user.shop_url,
      shopname: this.$auth.user.shop_name,
    };
  },
  mounted() {
    let self = this;
    this.getOrderList();
  },
  methods: {
    cleanCurrOrder(){
      this.inv.data = null
      this.inv.inv_num = null
      this.inv.type = "india"
      this.inv.shipping_rate = null
      this.inv.shipping_tax = null
    },
    csvOrder() {
      window.URL = window.webkitURL || window.URL;
      let csv_data = [];

      this.currOrder.line_items.forEach((item) => {
        if (item.supp_qty != 0) {
          let row_str = [];
          row_str.push(item.title);

          row_str.push(item.quantity);
          row_str.push(parseFloat(item.price).toFixed(2));
          row_str.push(item.discount);
          row_str.push(item.tax);
          row_str.join(",");
          csv_data.push(row_str);
        }
      });
      csv_data = csv_data.join("\n");
      var contentType = "text/csv";

      var csvFile = new Blob([csv_data], { type: contentType });
      var a = document.createElement("a");
      a.download = "inv-csv.csv";
      a.href = window.URL.createObjectURL(csvFile);
      a.textContent = "Download CSV";

      a.dataset.downloadurl = [contentType, a.download, a.href].join(":");

      document.body.appendChild(a);
      a.click();
    },
    getOrderList() {
      this.$axios.get("/orders?type=" + this.order_type).then((response) => {
        if (this.order_type == "order") {
          this.orderlist = response.data.orders;
        } else {
          this.orderlist = response.data.checkouts;
        }
      });
    },
    setTax(tax) {
      if (this.currOrder) {
        this.currOrder.line_items.forEach((item) => {
          this.$set(item, "tax", String(tax));
          item.tax = tax;
        });
      }
    },
    setDis(dis) {
      if (this.currOrder) {
        this.currOrder.line_items.forEach((item) => {
          console.log(item.discount)
          this.$set(item, "discount", dis);
          item.discount = dis;
          console.log('~',item.discount)
        });
      }
    },
    updateShop() {
      let self = this;
      this.$axios
        .post("/update/user", {
          shop_url: this.shopurl,
          shop_name: this.shopname,
        })
        .then((response) => {
          if (response.data.success) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.success,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
          if (response.data.message) {
            self.$buefy.snackbar.open({
              duration: 4000,
              message: response.data.message,
              type: "is-light",
              position: "is-top-right",
              actionText: "Close",
              queue: true,
              onAction: () => {
                self.isActive = false;
              },
            });
          }
        });
    },
    printImg(row) {
      // this.currOrder = row;
      localStorage.setItem("order-img", JSON.stringify(row));
      window.open("/print/order-img", "_blank");
    },
    printImgChecked() {
      // this.currOrder = row;
      localStorage.setItem("order-img-list", JSON.stringify(this.checkedRows));
      window.open("/print/order-img-list", "_blank");
    },
    createInv(row) {
      this.currOrder = row;
      this.showInv = !this.showInv;
      let self = this;
      this.$axios.get("/get/order/" + row.order_number).then((response) => {
        console.log(response);
        let payload = response.data;
        if (Object.keys(payload).length != 0) {
          self.inv.shipping_rate = payload.shipping_rate;
          self.inv.shipping_tax = payload.shipping_tax;
          self.inv.type = payload.order_type;
          self.inv.date = new Date(payload.inv_date);
          self.inv.inv_num = payload.firm_order_id;
          // this.$set(item, "tax", row.tax);
          this.currOrder.line_items.forEach((item) => {
            payload.item.forEach((row) => {
              if (row.unq_item_id == item.unq_item_id) {
                // item.tax = row.tax;
                this.$set(item, "tax", row.tax);
                this.$set(item, "discount", row.discount);
                // item.discount = row.discount;
              } else {
                this.$set(item, "tax", null);
                this.$set(item, "discount", null);
                // item.discount = row.discount;
              }
            });
          });
        }
      });
    },
    saveInv() {
      if (this.currOrder) {
        let payload = {
          details: this.inv,
          order: this.currOrder,
        };
        this.$axios.post("/orders/save", payload).then((response) => {
          if (response.status == 200) {
            console.log("Order saved");
          }
        });
      }
    },
    printInv(id) {
      let route = this.$router.resolve({
        path: "/print/" + String(id),
      });
      window.open(route.href, "_blank");
    },

    getProduct(id, index) {
      console.log("!!!---", index);

      let self = this;
      this.$axios.get(`/product/${id}`).then((response) => {
        // console.log( response.data.images[0].src)
        try {
          let image_src = response.data.images[0].src;
          self.order.line_items[index].image = image_src;
          this.order_img.push({ image_src, index });
          setTimeout(function () {}, 1500);
          // console.log("~", image_src);
          return image_src;
        } catch (error) {
          console.log(error);
          return null;
        }
      });
    },
  },
};
</script>
<style>
.accent-bk {
  background-color: #0a0a0a;
  position: absolute;
  top: 0;
  left: 0;
  z-index: -1;
  width: 100%;
  height: 200px;
  transform: translateY(-50px);
}

.box-x {
  /* box-shadow:  none !important; */
  /* border: 2px solid #cecece; */
  border-radius: 10px;
}
</style>