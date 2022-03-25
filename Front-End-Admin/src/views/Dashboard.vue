<template>
  <div class="card card-default">
    <div class="card-header">
      <h3 class="card-title">Dashboard</h3>
    </div>
    <!-- /.card-header -->
    <div class="card-body">
      <div class="row">
        <div class="col-md-12">
          <div class="row">
            <div class="col-sm-12 col-lg-4">
              <div class="row">
                <div class="col-sm-6">
                  <div class="callout callout-info">
                    <small class="text-muted">Users</small>
                    <br />
                    <strong class="h4">{{ data.member }}</strong>
                    <div class="chart-wrapper">
                      <canvas
                        id="sparkline-chart-1"
                        width="100"
                        height="30"
                      ></canvas>
                    </div>
                  </div>
                </div>
                <!--/.col-->
                <div class="col-sm-6">
                  <div class="callout callout-danger">
                    <small class="text-muted">Events</small>
                    <br />
                    <strong class="h4">{{ data?.event }}</strong>
                    <div class="chart-wrapper">
                      <canvas
                        id="sparkline-chart-2"
                        width="100"
                        height="30"
                      ></canvas>
                    </div>
                  </div>
                </div>

                <!--/.col-->
              </div>
              <!--/.row-->
            </div>
            <!--/.col-->
            <div class="col-sm-6 col-lg-4">
              <div class="row">
                <div class="col-sm-6">
                  <div class="callout callout-warning">
                    <small class="text-muted">News</small>
                    <br />
                    <strong class="h4">{{ data?.news }}</strong>
                    <div class="chart-wrapper">
                      <canvas
                        id="sparkline-chart-3"
                        width="100"
                        height="30"
                      ></canvas>
                    </div>
                  </div>
                </div>
                <!--/.col-->
                <div class="col-sm-6">
                  <div class="callout callout-success">
                    <small class="text-muted">Current active event</small>
                    <br />
                    <strong class="h4">{{ data?.current_active_event }}</strong>
                    <div class="chart-wrapper">
                      <canvas
                        id="sparkline-chart-4"
                        width="100"
                        height="30"
                      ></canvas>
                    </div>
                  </div>
                </div>
                <!--/.col-->
              </div>
              <!--/.row-->
            </div>
            <!--/.col-->
            <div class="col-sm-6 col-lg-4">
              <div class="row">
                <div class="col-sm-6">
                  <div class="callout">
                    <small class="text-muted">Attendance average</small>
                    <br />
                    <strong class="h4">{{ data?.check_average }}</strong>
                    <div class="chart-wrapper">
                      <canvas
                        id="sparkline-chart-5"
                        width="100"
                        height="30"
                      ></canvas>
                    </div>
                  </div>
                </div>
                <!--/.col-->
                
                <!--/.col-->
              </div>
              <!--/.row-->
            </div>
            <div class="col-sm-12 my-12">
              <ul class="horizontal-bars type-2">
                <li>
                  <i class="icon-user"></i>
                  <span class="title">Male</span>
                  <span class="value">{{ data.gender?.male }}</span>
                  <div class="bars">
                    <div class="progress progress-xs">
                      <div
                        class="progress-bar bg-warning"
                        role="progressbar"
                        :style="'width: ' + data.gender?.male_raw + '%'"
                        aria-valuenow="43"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                </li>
                <li>
                  <i class="icon-user-female"></i>
                  <span class="title">Female</span>
                  <span class="value">{{ data?.gender?.female }}</span>
                  <div class="bars">
                    <div class="progress progress-xs">
                      <div
                        class="progress-bar bg-warning"
                        role="progressbar"
                        :style="'width: ' + data.gender?.female_raw + '%'"
                        aria-valuenow="37"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                </li>
                <li class="divider"></li>
              </ul>
            </div>
            <div class="col-sm-12 my-12">
              <ul class="horizontal-bars type-2">
                <li>
                  <i class="icon-user"></i>
                  <span class="title">Client</span>
                  <span class="value">{{ data.role?.client }}</span>
                  <div class="bars">
                    <div class="progress progress-xs">
                      <div
                        class="progress-bar bg-danger"
                        role="progressbar"
                        :style="'width: ' + data.role?.client_raw + '%'"
                        aria-valuenow="43"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                </li>
                <li>
                  <i class="icon-user-female"></i>
                  <span class="title">Admin</span>
                  <span class="value">{{ data?.role?.admin }}</span>
                  <div class="bars">
                    <div class="progress progress-xs">
                      <div
                        class="progress-bar bg-danger"
                        role="progressbar"
                        :style="'width: ' + data.role?.admin_raw + '%'"
                        aria-valuenow="37"
                        aria-valuemin="0"
                        aria-valuemax="100"
                      ></div>
                    </div>
                  </div>
                </li>
                <li class="divider"></li>
              </ul>
            </div>
            <!--/.col-->
          </div>
        </div>
      </div>
      <!-- /.row -->
      <!-- /.row -->
    </div>
    <!-- /.card-body -->
  </div>
</template>

<script>
import { mapMutations } from "vuex";
import { BREADCRUMB } from "@/store/storeconstants";
import EventDataService from "@/services/EventDataService";

export default {
  data() {
    return {
      data: {},
    };
  },
  created() {
    document.title = "Dashboard";
    this.breadcrumb("Dashboard");
    this.getDashboard();
  },
  methods: {
    ...mapMutations({
      breadcrumb: BREADCRUMB,
    }),
    getDashboard() {
      EventDataService.getDashboard().then((res) => {
        console.log(res);
        // console.log(res);
        this.data = res.data;
      });
    },
  },
};
</script>

<style>
</style>