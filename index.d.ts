declare module "node-libuiohook" {
    export = NodeLibuiohook;

    namespace NodeLibuiohook {
        type TKeyEventType = "registerKeydown" | "registerKeyup";

        interface INodeLibuiohookBinding {
            callback?: () => void;
            eventType: TKeyEventType;
            key?: string; // Is key code
            keyCode?: number; // Is key code
            modifiers?: {
                alt: boolean;
                ctrl: boolean;
                shift: boolean;
                meta: boolean;
            };
        }

        export function startHook(): void;
        export function stopHook(): void;
        export function registerCallback(binding: INodeLibuiohookBinding): void;
        export function unregisterCallback(binding: INodeLibuiohookBinding): void;
    }
}
