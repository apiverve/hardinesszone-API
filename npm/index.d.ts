declare module '@apiverve/hardinesszone' {
  export interface hardinesszoneOptions {
    api_key: string;
    secure?: boolean;
  }

  export interface hardinesszoneResponse {
    status: string;
    error: string | null;
    data: USDAHardinessZoneData;
    code?: number;
  }


  interface USDAHardinessZoneData {
      zipCode:   string;
      zone:      string;
      tempRange: string;
      zoneTitle: string;
      details:   Details;
  }
  
  interface Details {
      tempRange:     string;
      description:   string;
      plantSurvival: string;
  }

  export default class hardinesszoneWrapper {
    constructor(options: hardinesszoneOptions);

    execute(callback: (error: any, data: hardinesszoneResponse | null) => void): Promise<hardinesszoneResponse>;
    execute(query: Record<string, any>, callback: (error: any, data: hardinesszoneResponse | null) => void): Promise<hardinesszoneResponse>;
    execute(query?: Record<string, any>): Promise<hardinesszoneResponse>;
  }
}
