using System;
using System.Collections.Generic;
using System.Text;
using Newtonsoft.Json;

namespace APIVerve.API.USDAHardinessZone
{
    /// <summary>
    /// Query options for the USDA Hardiness Zone API
    /// </summary>
    public class USDAHardinessZoneQueryOptions
    {
        /// <summary>
        /// The zip code to get the USDA Plant Hardiness Zone for
        /// Example: 97201
        /// </summary>
        [JsonProperty("zip")]
        public string Zip { get; set; }
    }
}
