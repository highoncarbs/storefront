<template>
  <section v-if="order" class="section container my-0 py-0">
    <div class="level">
      <div class="level-left">
        <img :src="'/uploads/' + logopath" width="150" alt="" />
      </div>
      <div class="level-right">
        <h2 class="is-size-5 has-text-weight-bold">Tax Invoice</h2>
      </div>
    </div>

    <table
      v-if="firm.name"
      class="mt-3 mb-0 table is-bordered is-narrow is-fullwidth"
    >
      <colgroup>
        <col span="50%" />
        <col span="50%" />
      </colgroup>

      <tbody>
        <tr>
          <td>
            <!-- Sender Details -->
            <p class="heading">SENDER</p>
            <p>{{ firm.name }}</p>
            <p>{{ firm.address }}</p>
            <p>Ph. No - {{ firm.phone }}</p>
            <p>
              <span class="has-text-weight-bold">GSTIN</span> -
              {{ firm.gst.toUpperCase() }}
            </p>
          </td>
          <td>
            <!-- Sender Details -->
            <p class="heading"></p>
            <p>
              <span class="has-text-weight-bold mr-2"> Order Code </span>
              ITM/SHP-{{ order.shopify_order_id }}
            </p>
            <p>
              <span class="has-text-weight-bold mr-2"> Invoice No. </span>
              ITM-{{ order.firm_order_id }}
            </p>
            <p>
              <span class="has-text-weight-bold mr-2"> Invoice Date </span>
              {{
                new Date(order.inv_date).toLocaleDateString("en-IN", {
                  year: "numeric",
                  month: "short",
                  day: "numeric",
                })
              }}
            </p>
          </td>
        </tr>
        <tr>
          <td>
            <!-- Sender Details -->
            <p class="heading">BILL TO</p>
            <p class="has-text-weight-bold">{{ order.customer_name }}</p>
            <p>{{ JSON.parse(order.customer_address).address1 }}</p>
            <p>{{ JSON.parse(order.customer_address).address2 }}</p>
            <p>
              {{
                JSON.parse(order.customer_address).city +
                " - " +
                JSON.parse(order.customer_address).zip
              }}
            </p>
            <p>
              {{
                JSON.parse(order.customer_address).province +
                ", " +
                JSON.parse(order.customer_address).country
              }}
            </p>
            <p>
              <span class="has-text-weight-bold">Ph. No</span>

              {{ order.customer_phone }}
            </p>
            <p>
              <span class="has-text-weight-bold">Email</span>
              {{ order.customer_email }}
            </p>
            <p class="is-uppercase" v-if="order.customer_gst">
              <span class="has-text-weight-bold">GST</span>
              {{ order.customer_gst }}
            </p>
          </td>
          <td>
            <!-- Sender Details -->
            <p class="heading">SHIP TO</p>
            <p class="has-text-weight-bold">{{ order.customer_name }}</p>
            <p>{{ JSON.parse(order.shipping_address).address1 }}</p>
            <p>{{ JSON.parse(order.shipping_address).address2 }}</p>
            <p>
              {{
                JSON.parse(order.shipping_address).city +
                " - " +
                JSON.parse(order.shipping_address).zip
              }}
            </p>
            <p>
              {{
                JSON.parse(order.shipping_address).province +
                ", " +
                JSON.parse(order.shipping_address).country
              }}
            </p>
            <p>
              <span class="has-text-weight-bold">Ph. No</span>

              {{ order.customer_phone }}
            </p>
            <p>
              <span class="has-text-weight-bold">Email</span>
              {{ order.customer_email }}
            </p>
          </td>
        </tr>
      </tbody>
    </table>
    <table class="mt-3 mb-0 table is-bordered is-narrow is-fullwidth">
      <!-- <colgroup>
        <col span="50%" />
        <col span="50%" />
      </colgroup> -->
      <thead>
        <th>S. No</th>
        <th>Description of Goods</th>
        <th>Qty<br>(pc/mtr)</th>
        <th>Rate <br />(INR)</th>
        <th>Discount</th>
        <th>Discounted Rate</th>
        <th>Taxable Amount<br />(INR)</th>
        <th v-if="order.order_type == 'india' || order.order_type == 'export'">
          GST %
        </th>
        <th v-if="order.order_type == 'intra'">SCGST %</th>
        <th v-if="order.order_type == 'intra'">SGST Tax</th>
        <th v-if="order.order_type == 'intra'">CGST %</th>
        <th v-if="order.order_type == 'intra'">CGST Tax</th>
        <th>GST Amt.</th>
        <th>Amount<br />(INR)</th>
      </thead>
      <tbody>
        <tr :key="index" v-for="(item, index) in order.item">
          <td>{{ index + 1 }}</td>
          <td>{{ item.name }}</td>
          <td>{{ item.qty }}</td>
          <td>
            {{ getPreTaxRate(item).toFixed(2) }}
          </td>
          <td>{{ item.discount }}</td>
          <td>
            {{ getDiscountRate(item) }}
          </td>
          <td>
            {{ (getDiscountRate(item) * item.qty).toFixed(2) }}
          </td>
          <td v-if="order.order_type == 'india'">{{ item.tax }}</td>
          <td v-if="order.order_type == 'intra'">{{ item.tax / 2 }}</td>
          <td v-if="order.order_type == 'intra'">
            {{
              (
                parseFloat(
                  (item.price -
                    parseFloat(item.price / ((100 + Number(item.tax)) / 100))) /
                    2
                ) * item.qty
              ).toFixed(2)
            }}
          </td>
          <td v-if="order.order_type == 'intra'">{{ item.tax / 2 }}</td>
          <td v-if="order.order_type == 'intra'">
            {{
              (
                parseFloat(
                  (item.price -
                    parseFloat(item.price / ((100 + Number(item.tax)) / 100))) /
                    2
                ) * item.qty
              ).toFixed(2)
            }}
          </td>
          <td>
            {{
              (getDiscountRate(item) * item.qty * (item.tax / 100)).toFixed(2)
            }}
          </td>
          <td>{{ getLineItemRate(item) }}</td>
        </tr>
        <tr v-if="order.shipping_rate != 0 && order.shipping_rate != null">
          <td>{{ order.item.length + 1 }}</td>
          <td>Shipping</td>
          <td></td>
          <td></td>
          <!-- <td>{{order.shipping_rate}}</td> -->
          <td>
            {{
              parseFloat(
                order.shipping_rate / ((100 + Number(order.shipping_tax)) / 100)
              ).toFixed(2)
            }}
          </td>
          <td></td>
          <td>
            {{
              parseFloat(
                order.shipping_rate / ((100 + Number(order.shipping_tax)) / 100)
              ).toFixed(2)
            }}
          </td>
          <td
            v-if="order.order_type == 'india' || order.order_type == 'export'"
          >
            {{ order.shipping_tax }}
          </td>
          <td v-if="order.order_type == 'intra'">
            {{ order.shipping_tax / 2 }}
          </td>
          <td v-if="order.order_type == 'intra'">
            {{
              parseFloat(
                (order.shipping_rate -
                  parseFloat(
                    order.shipping_rate /
                      ((100 + Number(order.shipping_tax)) / 100)
                  )) /
                  2
              ).toFixed(2)
            }}
          </td>
          <td v-if="order.order_type == 'intra'">
            {{ order.shipping_tax / 2 }}
          </td>
          <td v-if="order.order_type == 'intra'">
            {{
              parseFloat(
                (order.shipping_rate -
                  parseFloat(
                    order.shipping_rate /
                      ((100 + Number(order.shipping_tax)) / 100)
                  )) /
                  2
              ).toFixed(2)
            }}
          </td>
          <td>
            {{
              parseFloat(
                order.shipping_rate -
                  parseFloat(
                    order.shipping_rate /
                      ((100 + Number(order.shipping_tax)) / 100)
                  )
              ).toFixed(2)
            }}
          </td>
          <td>{{ parseFloat(order.shipping_rate).toFixed(2) }}</td>
        </tr>
      </tbody>
      <tfoot>
        <tr>
          <td></td>
          <td>Total</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td>{{ getTotalTaxable() }}</td>
          <td
            v-if="order.order_type == 'india' || order.order_type == 'export'"
          ></td>
          <td v-if="order.order_type == 'intra'"></td>
          <td v-if="order.order_type == 'intra'"></td>
          <td v-if="order.order_type == 'intra'"></td>
          <td v-if="order.order_type == 'intra'"></td>
          <td>{{ getTotalTaxes() }}</td>
          <td>
            {{
              parseFloat(
                Number(order.total_bill) + Number(order.shipping_rate)
              ).toFixed(2)
            }}
          </td>
        </tr>
      </tfoot>
    </table>
    <br />
    <p class="">Amount Chargable (in words)</p>
    <p style="text-transform: capitalize" class="has-text-weight-bold">
      {{
        numtoWords(
          parseFloat(
            Number(order.total_bill) + Number(order.shipping_rate)
          ).toFixed(0)
        )
      }}
    </p>
    <br />
    <p class="has-text-weight-bold">Declaration</p>
    <p>
      1. We declare that this invoice shows the actual price of the goods
      described and that all particulars are true and correct.
    </p>
    <p>2. All Disputes are subject to Jaipur jurisdiction only.</p>
    <br />
    <p class="has-text-centered heading has-text-weight-bold">
      THIS IS A COMPUTER GENERATED Invoice
    </p>
  </section>
</template>

<script>
export default {
  layout: "empty",
  mounted() {
    this.$axios.get("get/user/firm").then((response) => {
      this.firm.name = response.data.firm_name;
      this.firm.gst = response.data.firm_gst;
      this.firm.phone = response.data.firm_phone;
      this.firm.address = response.data.firm_address;
      this.firm.order_start = response.data.order_start;
      this.logopath = response.data.image;
    });
    this.$axios.get("/get/order/" + this.$route.params.id).then((response) => {
      this.order = response.data;
      document.title =
        "ITM-" +
        this.order.firm_order_id +
        " - " +
        new Date(this.order.inv_date).toLocaleDateString("en-in") +
        " - TAX";
    });
  },
  data() {
    return {
      firm: {
        name: null,
        gst: null,
        address: null,
        phone: null,
        order_start: null,
      },
      logopath: null,
      order: null,

      comapny_data: [],
      company: null,
      id: null,
      details: {},
    };
  },
  methods: {
    getPreTaxRate(item) {
      return item.price / ((100 + Number(item.tax)) / 100);
    },
    getDiscountRate(item) {
      if (item.discount && item.discount != 0) {
        return (this.getPreTaxRate(item) * (1 - item.discount / 100)).toFixed(
          2
        );
      } else {
        return this.getPreTaxRate(item).toFixed(2);
      }
    },
    getLineItemRate(item) {
      return (
        this.getDiscountRate(item) * item.qty +
        this.getDiscountRate(item) * item.qty * (item.tax / 100)
      ).toFixed(2);
    },
    getTotalRate() {
      let total = 0.0;
      this.order.item.forEach((item) => {
        total +=
          parseFloat(item.price / ((100 + Number(item.tax)) / 100)) * item.qty;
      });
      return parseFloat(total).toFixed(2);
    },
    getTotalTaxes() {
      let total = 0.0;
      this.order.item.forEach((item) => {
        total += this.getDiscountRate(item) * item.qty * (item.tax / 100)
      });
      if(this.order.shipping_rate != 0 ){

        total +=
        this.order.shipping_rate -
        parseFloat(
            this.order.shipping_rate /
            ((100 + Number(this.order.shipping_tax)) / 100)
        );
        }
      return parseFloat(total).toFixed(2);
    },
    getTotalTaxable() {
      let total = 0.0;
      this.order.item.forEach((item) => {
        total += this.getDiscountRate(item) * item.qty;
      });
      total +=
        this.order.shipping_rate -
        parseFloat(
          this.order.shipping_rate /
            ((100 + Number(this.order.shipping_tax)) / 100)
        );
      return parseFloat(total).toFixed(2);
    },

    numtoWords(num) {
      var a = [
        "",
        "one ",
        "two ",
        "three ",
        "four ",
        "five ",
        "six ",
        "seven ",
        "eight ",
        "nine ",
        "ten ",
        "eleven ",
        "twelve ",
        "thirteen ",
        "fourteen ",
        "fifteen ",
        "sixteen ",
        "seventeen ",
        "eighteen ",
        "nineteen ",
      ];
      var b = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
      ];

      if ((num = Number(num).toString()).length > 9) return "overflow";
      let n = ("000000000" + num)
        .substr(-9)
        .match(/^(\d{2})(\d{2})(\d{2})(\d{1})(\d{2})$/);
      if (!n) return;
      var str = "";
      str +=
        n[1] != 0
          ? (a[Number(n[1])] || b[n[1][0]] + " " + a[n[1][1]]) + "crore "
          : "";
      str +=
        n[2] != 0
          ? (a[Number(n[2])] || b[n[2][0]] + " " + a[n[2][1]]) + "lakh "
          : "";
      str +=
        n[3] != 0
          ? (a[Number(n[3])] || b[n[3][0]] + " " + a[n[3][1]]) + "thousand "
          : "";
      str +=
        n[4] != 0
          ? (a[Number(n[4])] || b[n[4][0]] + " " + a[n[4][1]]) + "hundred "
          : "";
      str +=
        n[5] != 0
          ? (str != "" ? "and " : "") +
            (a[Number(n[5])] || b[n[5][0]] + " " + a[n[5][1]]) +
            "only "
          : "";
      return str;
    },
  },
};
</script>


<style scoped>
@media print {
  @page {
    size: portrait;
  }
}

body,
p {
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.3;
  background: #fff !important;
  color: #000;
}

h1 {
  font-size: 24pt;
}

p,
td,
th {
  font-size: 10pt !important;
}
h2,
h3,
h4 {
  font-size: 14pt;
  margin-top: 25px;
}
h2 {
  font-size: 12pt;
}
</style>