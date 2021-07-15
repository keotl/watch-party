export const SET_URL = "SET_URL";

export type SetUrlAction = {
    type: typeof SET_URL;
    url: string;
}

export function setUrlAction(url: string,): SetUrlAction {
    return {
	type: SET_URL,
	url
    }
}
