//All Fields are required
export interface UserConfig {
    configId: number;
    systemName: string;
    propertyKey: string;
    configKey: string;
    configValue: string;
    updatedDate: Date; // New configs are set to current date
    updatedBy: string;

}