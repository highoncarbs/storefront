<template>
  <div class="section container my-0 py-0" v-if="order">
    <table class="mt-3 mb-0 table is-bordered is-narrow is-fullwidth">
      <colgroup>
        <col span="20%" />
        <col span="20%" />
        <col span="30%" />
        <col span="30%" />
      </colgroup>
      <tbody>
        <tr>
          <td colspan="4">
            <h4 class="has-text-weight-bold has-text-centered">
              EXPORT INVOICE
            </h4>
          </td>
        </tr>
        <tr>
          <td colspan="2" rowspan="3">
            <p class="has-text-weight-bold">Exporter</p>
            <!-- <div v-if="company">
              <p>{{ company.name.toUpperCase() }}</p>
              <p v-for="(row , idx) in company.address.split('\n')" :key="idx">{{row.toUpperCase() }}</p>
              <p>PH: {{ company.phone.toUpperCase() }}</p>
              <p>EMAIL: {{ company.email.toUpperCase() }}</p>
            </div> -->
          </td>
          <td colspan="1">
            <p>
              <span class="has-text-weight-bold"> Invoice No.</span>
              <span class="mr-2">{{ details.transport.inv_num }} </span>
              <span class="has-text-weight-bold">Date :</span>
              <span>
                {{
                  new Date(details.transport.inv_date).toLocaleDateString(
                    "en-IN",
                    {
                      day: "numeric",
                      month: "short",
                      year: "numeric",
                    }
                  )
                }}</span
              >
            </p>
          </td>
          <td colspan="1">
            <p>
              <span class="has-text-weight-bold"> IEC CODE NO. </span>
              <span>{{ company.iec.toUpperCase() }}</span>
            </p>
          </td>
        </tr>
        <tr>
          <td colspan="2">
            <span class="has-text-weight-bold"> Buyer Ref </span>
          </td>
        </tr>
        <tr>
          <td colspan="2">
            <p class="has-text-weight-bold">Other Ref</p>
            <p>
              <span class="has-text-weight-bold"> PAN </span>
              {{ company.pan.toUpperCase() }}
            </p>
            <p>
              <span class="has-text-weight-bold"> REX </span>
              {{ company.rex.toUpperCase() }}
            </p>
          </td>
        </tr>
        <!-- Consignee Address -->
        <tr>
          <td colspan="2" rowspan="2">
            <p class="has-text-weight-bold">Consignee</p>
            <div>
              <p>{{ order.user.username.toUpperCase() }}</p>
              <p>{{ order.user.shp_address.toUpperCase() }}</p>
              <p>{{ order.user.shp_city.toUpperCase() }} - {{ order.user.shp_zipcode }}</p>
              <p>{{ order.user.shp_country.toUpperCase() }}</p>
              <p>{{ order.user.phone }}</p>
              <p>{{ order.user.email.toUpperCase() }}</p>
            </div>
    
          </td>
          <td colspan="2">
            <p class="has-text-weight-bold">Buyer</p>
            <p>Same as Consignee</p>
          </td>
        </tr>
        <tr>
          <td>
            <span class="has-text-weight-bold"> Country of Origin</span>
            <p>INDIA</p>
          </td>
          <td>
            <span class="has-text-weight-bold"> Destination Country</span>
            <p>
              {{ order.user.country.toUpperCase() }}
            </p>
          </td>
        </tr>
        <!-- Extra Info - Shipping , Terms & conditions -->
        <tr>
          <td>
          <p class="has-text-weight-bold">Pre-Carriage By</p>
            <p>BY AIR</p>
            <br />
          </td>
          <td>
            <p class="has-text-weight-bold">Place of Recipt</p>
            <br />
          </td>
          <td colspan="2" rowspan="3">
            <p class="has-text-weight-bold">Terms of delivery & Payment</p>
            <p>{{ this.details.transport.terms }}</p>
          </td>
        </tr>
        <tr>
          <td>
            <p class="has-text-weight-bold">Vessel/Flight</p>
            <br />
          </td>
          <td>
            <p class="has-text-weight-bold">Port of Loading</p>
            <br />
          </td>
        </tr>
        <tr>
          <td>
            <p class="has-text-weight-bold">Port of Discharge</p>
            <br />
          </td>
          <td>
            <p class="has-text-weight-bold">Place of Delivery</p>
            <br />
          </td>
        </tr>
        <tr>
          <td colspan="1">
            <p class="has-text-weight-bold">No & Kind of Pkgs.</p>
            <p>{{ details.transport.box }}</p>
          </td>
          <td colspan="3">
            <p class="has-text-weight-bold">Description of Goods</p>
            <p>{{ details.transport.ex_desc }}</p>
          </td>
        </tr>
      </tbody>
    </table>
    <table class="mt-3 mb-0 table is-bordered is-narrow is-fullwidth">
      <colgroup>
        <col span="5%" />
        <col span="10%" />
        <col span="20%" />
        <col span="10%" />
        <col span="10%" />
        <col span="5%" />
        <col span="5%" />
        <col span="5%" />
        <col span="5%" />
        <col span="10%" />
      </colgroup>
      <tbody>
        <tr class="has-text-centered">
          <td class="has-text-weight-bold">S.No.</td>
          <td class="has-text-weight-bold">Style No.</td>
          <td class="has-text-weight-bold">Description of Goods</td>
          <td class="has-text-weight-bold">HSN Code</td>
          <td class="has-text-weight-bold">Sq. mtr</td>
          <td class="has-text-weight-bold">
            <span> Net wt. per </span> <br />
            <span> mtr in Kg </span>
          </td>
          <td class="has-text-weight-bold">UOM</td>
          <td class="has-text-weight-bold">Qty</td>
          <td class="has-text-weight-bold">
            <span> Rate </span> <br />
            <span>{{ details.transport.contract }}</span> <br />
            <span>{{ details.currency.name }}</span>
          </td>
          <td class="has-text-weight-bold">
            <span> Amount </span> <br />
            <span>{{ details.transport.contract }}</span> <br />
            <span>{{ details.currency.name }}</span>
          </td>
        </tr>
        <tr :key="index" v-for="(item, index) in order.item">
          <td>{{ index + 1 }}</td>
          <td>{{ item.item[0].gen_name +'/'+ item.item[0].sku }}</td>
          <td>{{ item.hsn_desc }}</td>
          <td class="has-text-right">{{ item.item[0].hsn[0].name }}</td>
          <td class="has-text-right">{{ JSON.parse(item.meta).sq }}</td>
          <td class="has-text-right">{{ JSON.parse(item.meta).wt }}</td>

          <td>{{ item.item[0].uom[0].name }}</td>
          <td class="has-text-right">
            {{ parseFloat(item.supp_qty).toFixed(2) }}
          </td>
          <td class="has-text-right">
            {{ getPriceBy(item.item[0], details.currency) }}
          </td>
          <td class="has-text-right">
            {{
              parseFloat(
                getPriceBy(item.item[0], details.currency) * item.supp_qty
              ).toFixed(2)
            }}
          </td>
        </tr>
        <tr>
          <td>{{ order.item.length + 1 }}</td>
          <td>Shipping Charges</td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>
          <td></td>

          <td></td>
          <td></td>

          <td class="has-text-right">
            {{ parseFloat(details.transport.rate).toFixed(2) }}
          </td>
        </tr>
        <tr>
          <td colspan="8">
            <span class="has-text-weight-bold ml-3">
              Amount Chargable ( in words )  {{ details.currency.name }}
            </span>
            {{ (numtoWords(Math.ceil(totalAmt()))).toUpperCase() }}
          </td>
          <td class="has-text-weight-bold">TOTAL</td>
          <td class="has-text-right">{{ totalAmt() }}</td>
        </tr>

        <tr>
          <td colspan="7">
            <table class="has-border-none">
              <tr>
                <td>
                  <span class="mr-3 has-text-weight-bold">Bank A/C Name</span>
                </td>
                <td>
                  {{ company.ac_name }}
                </td>
              </tr>
              <tr>
                <td>
                  <span class="mr-3 has-text-weight-bold">Name of Bank</span>
                </td>
                <td>
                  {{ company.bank_name }}
                </td>
              </tr>
              <tr>
                <td>
                  <span class="mr-3 has-text-weight-bold">Current A/C #</span>
                </td>
                <td>
                  {{ company.ac_no }}
                </td>
              </tr>
              <tr>
                <td>
                  <span class="mr-3 has-text-weight-bold">SWIFT</span>
                </td>
                <td>
                  {{ company.swift.toUpperCase() }}
                </td>
              </tr>
            </table>

            <p class="mt-2">Declaration:</p>
          <p>
              1. We declare that this Invoice shows the actual price of the goods
            described and that all particulars are true and correct.</p>
         </td>
          <td colspan="7">
            <p>For {{ titleCase(company.name) }}</p>
            <p style="bottom: 3px;
    position: absolute;">AUTHORISED SIGNATORY</p>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  layout: "empty",
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

     
    };
  },
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
    });
  },
  methods: {
  getTotalRate() {
      let total = 0.0;
      this.order.item.forEach((item) => {
        total += parseFloat(item.price / ((100 + Number(item.tax)) / 100));
      });
      return parseFloat(total).toFixed(2);
    },
    getTotalTaxable() {
      let total = 0.0;
      this.order.item.forEach((item) => {
        total +=
          item.price -
          parseFloat(item.price / ((100 + Number(item.tax)) / 100));
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
    //   REmove OLD CODE
    totalAmt() {
      let total = Number(0.0);
      this.order.item.forEach((item) => {
        total += Number(
          this.getPriceBy(item.item[0], this.details.currency) * item.supp_qty
        );
      });
      total += Number(this.details.transport.rate);
      return parseFloat(total).toFixed(2);
    },
  },
};
</script><style scoped>
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