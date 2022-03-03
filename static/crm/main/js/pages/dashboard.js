//[Dashboard Javascript]

//Project:	Sunny Admin - Responsive Admin Template
//Primary use:   Used only for the main dashboard (index.html)


$(function () {

  'use strict';

	var options = {
          series: [44, 55],
          chart: {
          type: 'donut',
			 height: 150,
			  width: 150,
        },
		legend: {
      		show: false,
		},
		dataLabels: {
			enabled: false,
		  },
		plotOptions: {
			pie: {
			  customScale: 0.8,
			  donut: {
				size: '50%',
			  },
			  offsetY: 0,
			},
			stroke: {
			  colors: undefined
			}
		  },
		colors:['#00BC8B', '#0F5EF7'],
        };

        var chart = new ApexCharts(document.querySelector("#chart41"), options);
        chart.render();

	var options = {
          series: [44, 55],
          chart: {
          type: 'donut',
			 height: 150,
			  width: 150,
        },
		legend: {
      		show: false,
		},
		dataLabels: {
			enabled: false,
		  },
		plotOptions: {
			pie: {
			  customScale: 0.8,
			  donut: {
				size: '50%',
			  },
			  offsetY: 0,
			},
			stroke: {
			  colors: undefined
			}
		  },
		colors:['#0F5EF7', '#00BC8B'],
        };

        var chart = new ApexCharts(document.querySelector("#chart42"), options);
        chart.render();

	// var options = {
    //     series: [{
    //         name: "Leads",
    //         data: [0, 40, 110, 70, 100, 60, 130, 55, 140, 75,120, 160]
    //     }],
    //     chart: {
	// 		foreColor:"#bac0c7",
    //       height: 385,
    //       type: 'line',
    //       zoom: {
    //         enabled: false
    //       }
    //     },
	// 	colors:['#0F5EF7'],
    //     dataLabels: {
    //       enabled: false,
    //     },
    //     stroke: {
    //       	show: true,
	// 		curve: 'smooth',
	// 		lineCap: 'butt',
	// 		colors: undefined,
	// 		width: 5,
	// 		dashArray: 0,
    //     },
	// 	markers: {
	// 		size: 5,
	// 		colors: '#ffffff',
	// 		strokeColors: '#0F5EF7',
	// 		strokeWidth: 3,
	// 		strokeOpacity: 0.9,
	// 		strokeDashArray: 0,
	// 		fillOpacity: 1,
	// 		discrete: [],
	// 		shape: "circle",
	// 		radius: 5,
	// 		offsetX: 0,
	// 		offsetY: 0,
	// 		onClick: undefined,
	// 		onDblClick: undefined,
	// 		hover: {
	// 		  size: undefined,
	// 		  sizeOffset: 3
	// 		}
	// 	},
    //     grid: {
	// 		borderColor: '#f7f7f7',
    //       row: {
    //         colors: ['transparent'], // takes an array which will be repeated on columns
    //         opacity: 0
    //       },
	// 	  yaxis: {
	// 		lines: {
	// 		  show: true,
	// 		},
	// 	  },
    //     },
    //     xaxis: {
    //       categories: ['Yan', 'Fev', 'Mar', 'Apr', 'May', 'Iyun', 'Iyul', 'Avg', 'Sen', 'Okt', 'Noy', 'Dek'],
	// 	  labels: {
	// 		show: true,
    //       },
    //       axisBorder: {
    //         show: true
    //       },
    //       axisTicks: {
    //         show: true
    //       },
    //       tooltip: {
    //         enabled: true,
    //       },
    //     },
    //     yaxis: {
    //       labels: {
    //         show: true,
    //         formatter: function (val) {
    //           return val;
    //         }
    //       }
	//
    //     },
    //   };
    //   var chart = new ApexCharts(document.querySelector("#charts_widget_43_chart"), options);
    //   chart.render();
	//
	//
	
	var options = {
          series: [{
            name: "Revenue",
            data: [60, 71, 75, 91, 80, 70]
        }],
          chart: {
          height: 150,
          type: 'area',
          zoom: {
            enabled: false
          },			  
		  toolbar: {
			show: false,
		  }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'stepline'
        },
		colors: ['#7a15f7'],
        grid: {			
			show: false,
			padding: {
			  top: 0,
			  bottom: -20,
			  right: 0,
			  left: -10
			},
        },
		
		 legend: {
      		show: false,
		 },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
			labels: {
          		show: false,
			},
			axisBorder: {
          		show: false,
			},
			axisTicks: {
          		show: false,
			},
        	},
		
        yaxis: {
          labels: {
          		show: false,
			}
        },
        };

        var chart = new ApexCharts(document.querySelector("#revenue1"), options);
        chart.render();
	
	
	
	
	
	var options = {
          series: [{
            name: "Revenue",
            data: [91, 80, 70, 60, 71, 75]
        }],
          chart: {
          height: 150,
          type: 'area',
          zoom: {
            enabled: false
          },			  
		  toolbar: {
			show: false,
		  }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'stepline'
        },
		colors: ['#FFB800'],
        grid: {			
			show: false,
			padding: {
			  top: 0,
			  bottom: -20,
			  right: 0,
			  left: -10
			},
        },
		
		 legend: {
      		show: false,
		 },
        xaxis: {
          categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
			labels: {
          		show: false,
			},
			axisBorder: {
          		show: false,
			},
			axisTicks: {
          		show: false,
			},
        	},
		
        yaxis: {
          labels: {
          		show: false,
			}
        },
        };

        var chart = new ApexCharts(document.querySelector("#revenue2"), options);
        chart.render();

		// var options = {
        //   series: [{
        //   name: 'Tashrif buyuruvchilar',
        //   data: [44, 55, 57, 56, 61, 58, 63, 101, 98, 87, 105, 91]
        // }, {
        //   name: 'Mijozlar',
        //   data: [76, 85, 101, 98, 87, 105, 91, 76, 85, 101, 98, 87]
        // }, {
        //   name: 'Savdolar',
        //   data: [98, 87, 105, 91, 76, 85, 76, 85, 101, 98, 87, 105]
        // }],
        //   chart: {
        //   type: 'bar',
		//   foreColor:"#bac0c7",
        //   height: 290,
		// 	  toolbar: {
        // 		show: false,
		// 	  }
        // },
        // plotOptions: {
        //   bar: {
        //     horizontal: false,
        //     columnWidth: '30%',
        //     endingShape: 'rounded'
        //   },
        // },
        // dataLabels: {
        //   enabled: false,
        // },
		// grid: {
		// 	show: true,
		// },
        // stroke: {
        //   show: true,
        //   width: 2,
        //   colors: ['transparent']
        // },
		// colors: ['#EF3737', '#0F5EF7', '#00cc00'],
        // xaxis: {
        //   categories: ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'Iyun', 'Iyul', 'Avgust', 'Sentabr', 'Oktabr', 'Noyabr', 'Dekabr'],
		//
        // },
        // yaxis: {
        //
        // },
		//  legend: {
      	// 	show: false,
		//  },
        // fill: {
        //   opacity: 1
        // },
        // tooltip: {
        //   y: {
        //     formatter: function (val) {
        //       return val
        //     }
        //   },
		// 	marker: {
		// 	  show: false,
		//   },
        // }
        // };
        //
        // var chart = new ApexCharts(document.querySelector("#recent_trend"), options);
        // chart.render();
	
	
	
}); // End of use strict
